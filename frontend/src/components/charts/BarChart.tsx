'use client';

import dynamic from 'next/dynamic';
import { ApexOptions } from 'apexcharts';

const Chart = dynamic(() => import('react-apexcharts'), { ssr: false });

interface BarChartProps {
  title?: string;
  categories: string[];
  series: { name: string; data: number[] }[];
  height?: number;
  colors?: string[];
}

export function BarChart({ 
  title, 
  categories, 
  series, 
  height = 350,
  colors = ['#3B82F6', '#10B981', '#F59E0B']
}: BarChartProps) {
  const options: ApexOptions = {
    chart: {
      type: 'bar',
      toolbar: {
        show: true,
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
    plotOptions: {
      bar: {
        horizontal: false,
        columnWidth: '55%',
        borderRadius: 4,
      },
    },
    dataLabels: {
      enabled: false,
    },
    stroke: {
      show: true,
      width: 2,
      colors: ['transparent'],
    },
    xaxis: {
      categories: categories,
    },
    yaxis: {
      title: {
        text: undefined,
      },
    },
    fill: {
      opacity: 1,
    },
    colors: colors,
    tooltip: {
      y: {
        formatter: function (val) {
          return val.toString();
        },
      },
    },
  };

  return (
    <div className="w-full">
      <Chart
        options={options}
        series={series}
        type="bar"
        height={height}
      />
    </div>
  );
}

