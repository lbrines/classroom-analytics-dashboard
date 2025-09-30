import { render, screen } from '@testing-library/react';
import { Input } from '../Input';

describe('Input', () => {
  it('renders input element', () => {
    render(<Input />);
    expect(screen.getByRole('textbox')).toBeInTheDocument();
  });

  it('renders with label', () => {
    render(<Input label="Test Label" />);
    expect(screen.getByLabelText('Test Label')).toBeInTheDocument();
  });

  it('shows error message', () => {
    render(<Input error="This is an error" />);
    expect(screen.getByText('This is an error')).toBeInTheDocument();
  });

  it('shows helper text', () => {
    render(<Input helperText="This is helper text" />);
    expect(screen.getByText('This is helper text')).toBeInTheDocument();
  });

  it('applies error styling when error is present', () => {
    render(<Input error="Error" />);
    const input = screen.getByRole('textbox');
    expect(input).toHaveClass('border-error-300');
  });

  it('can be disabled', () => {
    render(<Input disabled />);
    const input = screen.getByRole('textbox');
    expect(input).toBeDisabled();
  });

  it('accepts placeholder', () => {
    render(<Input placeholder="Enter text" />);
    expect(screen.getByPlaceholderText('Enter text')).toBeInTheDocument();
  });
});
