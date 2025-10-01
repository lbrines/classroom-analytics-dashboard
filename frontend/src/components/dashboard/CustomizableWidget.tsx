'use client';

import { useState, useRef, useCallback, useEffect } from 'react';
import { Card, CardContent, CardHeader, CardTitle } from '@/components/ui/Card';
import { Button } from '@/components/ui/Button';

interface WidgetConfig {
  id: string;
  type: string;
  title: string;
  position: { x: number; y: number };
  size: { width: number; height: number };
  config: Record<string, any>;
}

interface CustomizableWidgetProps {
  widget: WidgetConfig;
  onUpdate: (widget: WidgetConfig) => void;
  onDelete: (id: string) => void;
  children: React.ReactNode;
  isDragging?: boolean;
  onDragStart?: (e: React.DragEvent, widget: WidgetConfig) => void;
  onDragEnd?: () => void;
}

export function CustomizableWidget({
  widget,
  onUpdate,
  onDelete,
  children,
  isDragging = false,
  onDragStart,
  onDragEnd
}: CustomizableWidgetProps) {
  const [isResizing, setIsResizing] = useState(false);
  const [isConfiguring, setIsConfiguring] = useState(false);
  const widgetRef = useRef<HTMLDivElement>(null);
  const resizeRef = useRef<HTMLDivElement>(null);

  const handleMouseDown = (e: React.MouseEvent) => {
    if (e.target === resizeRef.current) {
      setIsResizing(true);
      e.preventDefault();
    }
  };

  const handleMouseMove = useCallback((e: MouseEvent) => {
    if (isResizing && widgetRef.current) {
      const rect = widgetRef.current.getBoundingClientRect();
      const newWidth = Math.max(200, e.clientX - rect.left);
      const newHeight = Math.max(150, e.clientY - rect.top);
      
      onUpdate({
        ...widget,
        size: { width: newWidth, height: newHeight }
      });
    }
  }, [isResizing, widget, onUpdate]);

  const handleMouseUp = () => {
    setIsResizing(false);
  };

  useEffect(() => {
    if (isResizing) {
      document.addEventListener('mousemove', handleMouseMove);
      document.addEventListener('mouseup', handleMouseUp);
      return () => {
        document.removeEventListener('mousemove', handleMouseMove);
        document.removeEventListener('mouseup', handleMouseUp);
      };
    }
  }, [isResizing, handleMouseMove]);

  const handleDragStart = (e: React.DragEvent) => {
    if (onDragStart) {
      onDragStart(e, widget);
    }
  };

  return (
    <div
      ref={widgetRef}
      className={`relative group ${isDragging ? 'opacity-50' : ''} ${isResizing ? 'cursor-resize' : ''}`}
      style={{
        width: widget.size.width,
        height: widget.size.height,
        transform: `translate(${widget.position.x}px, ${widget.position.y}px)`
      }}
      draggable
      onDragStart={handleDragStart}
      onDragEnd={onDragEnd}
      onMouseDown={handleMouseDown}
    >
      <Card className="h-full w-full">
        <CardHeader className="pb-2">
          <div className="flex items-center justify-between">
            <CardTitle className="text-sm font-medium">{widget.title}</CardTitle>
            <div className="flex items-center space-x-1 opacity-0 group-hover:opacity-100 transition-opacity">
              <Button
                size="sm"
                variant="ghost"
                onClick={() => setIsConfiguring(!isConfiguring)}
                className="h-6 w-6 p-0"
              >
                ⚙️
              </Button>
              <Button
                size="sm"
                variant="ghost"
                onClick={() => onDelete(widget.id)}
                className="h-6 w-6 p-0 text-red-500 hover:text-red-700"
              >
                ✕
              </Button>
            </div>
          </div>
        </CardHeader>
        
        <CardContent className="pt-0 flex-1">
          {isConfiguring ? (
            <div className="space-y-2">
              <div>
                <label className="block text-xs font-medium text-gray-700 mb-1">
                  Title
                </label>
                <input
                  type="text"
                  value={widget.title}
                  onChange={(e) => onUpdate({ ...widget, title: e.target.value })}
                  className="w-full px-2 py-1 text-xs border border-gray-300 rounded"
                />
              </div>
              <Button
                size="sm"
                onClick={() => setIsConfiguring(false)}
                className="w-full"
              >
                Save
              </Button>
            </div>
          ) : (
            <div className="h-full overflow-hidden">
              {children}
            </div>
          )}
        </CardContent>
        
        {/* Resize handle */}
        <div
          ref={resizeRef}
          className="absolute bottom-0 right-0 w-4 h-4 cursor-se-resize opacity-0 group-hover:opacity-100 transition-opacity"
          style={{
            background: 'linear-gradient(-45deg, transparent 0%, transparent 30%, #ccc 30%, #ccc 40%, transparent 40%, transparent 70%, #ccc 70%)'
          }}
        />
      </Card>
    </div>
  );
}
