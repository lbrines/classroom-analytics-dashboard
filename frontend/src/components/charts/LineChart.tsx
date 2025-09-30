'use client';

import dynamic from 'next/dynamic';
import { ApexOptions } from 'apexcharts';

const Chart = dynamic(() => import('react-apexcharts'), { ssr: false });

interface LineChartProps {
  title?: string;
  categories: string[];
  series: { name: string; data: number[] }[];
  height?: number;
  colors?: string[];
}

export function LineChart({ 
  title, 
  categories, 
  series, 
  height = 350,
  colors = ['#3B82F6', '#10B981', '#F59E0B']
}: LineChartProps) {
  const options: ApexOptions = {
    chart: {
      type: 'line',
      toolbar: {
        show: true,
      },
      zoom: {
        enabled: true,
      },
    },
    title: title ? {
      text: title,
      align: 'left',
      style: {
        fontSize: '16px',
        fontWeight: 600,
      },
    } : undefined,
    dataLabels: {
      enabled: false,
    },
    stroke: {
      curve: 'smooth',
      width: 3,
    },
    xaxis: {
      categories: categories,
    },
    yaxis: {
      title: {
        text: undefined,
      },
    },
    colors: colors,
    markers: {
      size: 4,
      hover: {
        size: 6,
      },
    },
    tooltip: {
      shared: true,
      intersect: false,
    },
    legend: {
      position: 'top',
      horizontalAlign: 'right',
    },
  };

  return (
    <div className="w-full">
      <Chart
        options={options}
        series={series}
        type="line"
        height={height}
      />
    </div>
  );
}

