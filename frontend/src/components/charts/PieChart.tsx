'use client';

import dynamic from 'next/dynamic';
import { ApexOptions } from 'apexcharts';

const Chart = dynamic(() => import('react-apexcharts'), { ssr: false });

interface PieChartProps {
  title?: string;
  labels: string[];
  series: number[];
  height?: number;
  colors?: string[];
}

export function PieChart({ 
  title, 
  labels, 
  series, 
  height = 350,
  colors = ['#3B82F6', '#10B981', '#F59E0B', '#EF4444', '#8B5CF6']
}: PieChartProps) {
  const options: ApexOptions = {
    chart: {
      type: 'pie',
    },
    title: title ? {
      text: title,
      align: 'left',
      style: {
        fontSize: '16px',
        fontWeight: 600,
      },
    } : undefined,
    labels: labels,
    colors: colors,
    legend: {
      position: 'bottom',
    },
    dataLabels: {
      enabled: true,
      formatter: function (val: number) {
        return val.toFixed(1) + '%';
      },
    },
    tooltip: {
      y: {
        formatter: function (val) {
          return val.toString();
        },
      },
    },
    responsive: [
      {
        breakpoint: 480,
        options: {
          chart: {
            width: 300,
          },
          legend: {
            position: 'bottom',
          },
        },
      },
    ],
  };

  return (
    <div className="w-full flex justify-center">
      <Chart
        options={options}
        series={series}
        type="pie"
        height={height}
      />
    </div>
  );
}

