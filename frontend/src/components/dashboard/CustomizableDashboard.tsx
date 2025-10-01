'use client';

import { useState, useEffect } from 'react';
import { CustomizableWidget } from './CustomizableWidget';
import { MetricCard } from './MetricCard';
import { ChartWidget } from './ChartWidget';
import { BarChart } from '@/components/charts/BarChart';
import { LineChart } from '@/components/charts/LineChart';
import { PieChart } from '@/components/charts/PieChart';
import { Button } from '@/components/ui/Button';
import { useMetrics } from '@/hooks/useMetrics';

interface WidgetConfig {
  id: string;
  type: string;
  title: string;
  position: { x: number; y: number };
  size: { width: number; height: number };
  config: Record<string, any>;
}

interface CustomizableDashboardProps {
  userId: string;
  role: string;
}

const DEFAULT_WIDGETS: WidgetConfig[] = [
  {
    id: 'metric-1',
    type: 'metric',
    title: 'Total Students',
    position: { x: 0, y: 0 },
    size: { width: 250, height: 120 },
    config: { metric: 'total_students', icon: '👥' }
  },
  {
    id: 'metric-2',
    type: 'metric',
    title: 'Active Courses',
    position: { x: 270, y: 0 },
    size: { width: 250, height: 120 },
    config: { metric: 'total_courses', icon: '📚' }
  },
  {
    id: 'chart-1',
    type: 'chart',
    title: 'Performance Overview',
    position: { x: 0, y: 140 },
    size: { width: 400, height: 300 },
    config: { chartType: 'bar', data: 'performance' }
  },
  {
    id: 'chart-2',
    type: 'chart',
    title: 'Trend Analysis',
    position: { x: 420, y: 140 },
    size: { width: 400, height: 300 },
    config: { chartType: 'line', data: 'trends' }
  }
];

export function CustomizableDashboard({ userId, role }: CustomizableDashboardProps) {
  const [widgets, setWidgets] = useState<WidgetConfig[]>(DEFAULT_WIDGETS);
  const [draggedWidget, setDraggedWidget] = useState<WidgetConfig | null>(null);
  const [isEditing, setIsEditing] = useState(false);
  const { metrics, isLoading } = useMetrics();

  // Load saved layout from localStorage
  useEffect(() => {
    const savedLayout = localStorage.getItem(`dashboard-layout-${userId}`);
    if (savedLayout) {
      try {
        const parsedLayout = JSON.parse(savedLayout);
        setWidgets(parsedLayout);
      } catch (error) {
        console.error('Failed to load saved layout:', error);
      }
    }
  }, [userId]);

  // Save layout to localStorage
  const saveLayout = () => {
    localStorage.setItem(`dashboard-layout-${userId}`, JSON.stringify(widgets));
  };

  const updateWidget = (updatedWidget: WidgetConfig) => {
    setWidgets(prev => prev.map(w => w.id === updatedWidget.id ? updatedWidget : w));
  };

  const deleteWidget = (widgetId: string) => {
    setWidgets(prev => prev.filter(w => w.id !== widgetId));
  };

  const handleDragStart = (e: React.DragEvent, widget: WidgetConfig) => {
    setDraggedWidget(widget);
    e.dataTransfer.effectAllowed = 'move';
  };

  const handleDragOver = (e: React.DragEvent) => {
    e.preventDefault();
    e.dataTransfer.dropEffect = 'move';
  };

  const handleDrop = (e: React.DragEvent) => {
    e.preventDefault();
    
    if (draggedWidget) {
      const rect = e.currentTarget.getBoundingClientRect();
      const x = e.clientX - rect.left;
      const y = e.clientY - rect.top;
      
      updateWidget({
        ...draggedWidget,
        position: { x, y }
      });
      
      setDraggedWidget(null);
    }
  };

  const addWidget = (type: string) => {
    const newWidget: WidgetConfig = {
      id: `widget-${Date.now()}`,
      type,
      title: `New ${type} Widget`,
      position: { x: 50, y: 50 },
      size: { width: 300, height: 200 },
      config: {}
    };
    
    setWidgets(prev => [...prev, newWidget]);
  };

  const renderWidgetContent = (widget: WidgetConfig) => {
    switch (widget.type) {
      case 'metric':
        return (
          <MetricCard
            title={widget.title}
            value={metrics?.overview?.[widget.config.metric] || 0}
            icon={<span className="text-2xl">{widget.config.icon}</span>}
            loading={isLoading}
          />
        );
      
      case 'chart':
        const chartProps = {
          height: widget.size.height - 100,
          loading: isLoading
        };
        
        switch (widget.config.chartType) {
          case 'bar':
            return (
              <ChartWidget title={widget.title} {...chartProps}>
                <BarChart
                  categories={['Course 1', 'Course 2', 'Course 3']}
                  series={[{ name: 'Completion Rate', data: [85, 72, 68] }]}
                  height={chartProps.height}
                />
              </ChartWidget>
            );
          
          case 'line':
            return (
              <ChartWidget title={widget.title} {...chartProps}>
                <LineChart
                  categories={['Jan', 'Feb', 'Mar', 'Apr', 'May']}
                  series={[{ name: 'Trend', data: [45, 52, 48, 55, 60] }]}
                  height={chartProps.height}
                />
              </ChartWidget>
            );
          
          case 'pie':
            return (
              <ChartWidget title={widget.title} {...chartProps}>
                <PieChart
                  labels={['Completed', 'In Progress', 'Pending']}
                  series={[60, 25, 15]}
                  height={chartProps.height}
                />
              </ChartWidget>
            );
          
          default:
            return <div className="p-4 text-gray-500">Unknown chart type</div>;
        }
      
      default:
        return <div className="p-4 text-gray-500">Unknown widget type</div>;
    }
  };

  return (
    <div className="relative min-h-screen bg-gray-50">
      {/* Toolbar */}
      <div className="bg-white border-b border-gray-200 p-4">
        <div className="flex items-center justify-between">
          <h2 className="text-lg font-semibold">Customizable Dashboard</h2>
          <div className="flex items-center space-x-2">
            <Button
              onClick={() => setIsEditing(!isEditing)}
              variant={isEditing ? "primary" : "outline"}
              size="sm"
            >
              {isEditing ? 'Exit Edit' : 'Edit Layout'}
            </Button>
            
            {isEditing && (
              <>
                <div className="border-l border-gray-300 h-6" />
                <Button
                  onClick={() => addWidget('metric')}
                  variant="outline"
                  size="sm"
                >
                  Add Metric
                </Button>
                <Button
                  onClick={() => addWidget('chart')}
                  variant="outline"
                  size="sm"
                >
                  Add Chart
                </Button>
                <Button
                  onClick={saveLayout}
                  variant="primary"
                  size="sm"
                >
                  Save Layout
                </Button>
              </>
            )}
          </div>
        </div>
      </div>

      {/* Dashboard Canvas */}
      <div
        className="relative p-4"
        onDragOver={handleDragOver}
        onDrop={handleDrop}
        style={{ minHeight: '600px' }}
      >
        {widgets.map(widget => (
          <CustomizableWidget
            key={widget.id}
            widget={widget}
            onUpdate={updateWidget}
            onDelete={deleteWidget}
            isDragging={draggedWidget?.id === widget.id}
            onDragStart={handleDragStart}
            onDragEnd={() => setDraggedWidget(null)}
          >
            {renderWidgetContent(widget)}
          </CustomizableWidget>
        ))}
        
        {widgets.length === 0 && (
          <div className="flex items-center justify-center h-64 text-gray-500">
            <div className="text-center">
              <p className="text-lg mb-2">No widgets added yet</p>
              <p className="text-sm">Click &quot;Edit Layout&quot; to add widgets to your dashboard</p>
            </div>
          </div>
        )}
      </div>
    </div>
  );
}
