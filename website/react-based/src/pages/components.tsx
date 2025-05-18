import React, { useState } from 'react';

interface ButtonProps {
  onClick?: () => void;
  children: React.ReactNode;
  className?: string;
  type?: 'button' | 'submit' | 'reset';
  dataIndex?: string;
}

export const Button: React.FC<ButtonProps> = ({ 
  onClick, 
  children, 
  className = '', 
  type = 'button',
  dataIndex
}) => {
  return (
    <button
      onClick={onClick}
      className={`btn cen ${className}`}
      type={type}
      data-index={dataIndex}
    >
      {children}
    </button>
  );
};

interface InputFieldProps {
  label: string;
  id: string;
  name: string;
  placeholder?: string;
  required?: boolean;
  value?: string;
  onChange?: (e: React.ChangeEvent<HTMLInputElement>) => void;
  type?: string;
  min?: number;
  max?: number;
  step?: number;
  hasPaste?: boolean;
}

export const InputField: React.FC<InputFieldProps> = ({
  label,
  id,
  name,
  placeholder = '',
  required = false,
  value,
  onChange,
  type = 'text',
  min,
  max,
  step,
  hasPaste = false
}) => {
  const handlePaste = () => {
    navigator.clipboard.readText().then(text => {
      const input = document.getElementById(id) as HTMLInputElement;
      if (input) {
        input.value = text;
        // Trigger change event
        const event = new Event('input', { bubbles: true });
        input.dispatchEvent(event);
      }
    });
  };

  return (
    <div className={`${name}_input flexed`}>
      <label htmlFor={id}>{label}</label>
      <input
        type={type}
        name={name}
        id={id}
        placeholder={placeholder}
        required={required}
        value={value}
        onChange={onChange}
        min={min}
        max={max}
        step={step}
      />
      {hasPaste && (
        <span className="paste" onClick={handlePaste}>
          <img alt="" className="paste-img" src="/static/icons/paste.svg" />
        </span>
      )}
    </div>
  );
};

interface FileInputProps {
  label: string;
  id: string;
  name: string;
  required?: boolean;
  onChange?: (e: React.ChangeEvent<HTMLInputElement>) => void;
}

export const FileInput: React.FC<FileInputProps> = ({
  label,
  id,
  name,
  required = false,
  onChange
}) => {
  return (
    <div className="encrypt_input flexed">
      <label htmlFor={id}>{label}</label>
      <input
        className="f-input"
        type="file"
        name={name}
        id={id}
        required={required}
        onChange={onChange}
      />
    </div>
  );
};

interface ResultDisplayProps {
  title: string;
  id: string;
  content?: string;
  className?: string;
}

export const ResultDisplay: React.FC<ResultDisplayProps> = ({
  title,
  id,
  content = '',
  className = ''
}) => {
  return (
    <div className={`results cen flex-col justify-center align-center f-gap-1 dark-glass mondia ${className}`}>
      <div className="cen">{title}</div>
      <div className={`generated-password ${id}-display`} id={`resultDiv${id}`}>
        {content.toString()}
      </div>
    </div>
  );
};

interface DropAreaProps {
  id: string;
  onDrop?: (files: FileList) => void;
}

export const DropArea: React.FC<DropAreaProps> = ({ id, onDrop }) => {
  const [isDragging, setIsDragging] = useState(false);

  const handleDragEnter = (e: React.DragEvent) => {
    e.preventDefault();
    e.stopPropagation();
    setIsDragging(true);
  };

  const handleDragOver = (e: React.DragEvent) => {
    e.preventDefault();
    e.stopPropagation();
  };

  const handleDragLeave = (e: React.DragEvent) => {
    e.preventDefault();
    e.stopPropagation();
    setIsDragging(false);
  };

  const handleDrop = (e: React.DragEvent) => {
    e.preventDefault();
    e.stopPropagation();
    setIsDragging(false);
    if (e.dataTransfer.files && e.dataTransfer.files.length > 0 && onDrop) {
      onDrop(e.dataTransfer.files);
    }
  };

  return (
    <div
      className={`dropArea flexed ${isDragging ? 'dragging' : ''}`}
      id={id}
      onDragEnter={handleDragEnter}
      onDragOver={handleDragOver}
      onDragLeave={handleDragLeave}
      onDrop={handleDrop}
    >
      or<br />Drag and drop files here
    </div>
  );
};

interface FAQItemProps {
  question: string;
  answer: React.ReactNode;
  faqNumber: string;
}

export const FAQItem: React.FC<FAQItemProps> = ({ question, answer, faqNumber }) => {
  const [isOpen, setIsOpen] = useState(false);

  return (
    <div className={`faq_qns faq${faqNumber}`}>
      <div className="qn flex justify-between" onClick={() => setIsOpen(!isOpen)}>
        {question}
        <div className="open-close flexed">
          {isOpen ? (
            <img src="/static/icons/up_arr.svg" alt="" className="upArrow" />
          ) : (
            <img src="/static/icons/dwn_arr.svg" alt="" className="downArrow" />
          )}
        </div>
      </div>
      <div className={`ans ${isOpen ? 'open' : ''}`}>
        {answer}
      </div>
    </div>
  );
};

interface LoaderProps {
  isLoading: boolean;
}

export const Loader: React.FC<LoaderProps> = ({ isLoading }) => {
  return (
    <div id="loader" className="loader-container" style={{ display: isLoading ? 'flex' : 'none' }}>
      <div className="loader"></div>
    </div>
  );
};

interface DarkModeToggleProps {
  isDarkMode: boolean;
  toggle: () => void;
}

export const DarkModeToggle: React.FC<DarkModeToggleProps> = ({ isDarkMode, toggle }) => {
  return (
    <div id="invert-button" className="invert-button flexed" onClick={toggle}>
      <div id="sun-icon" className={`sun flexed ${!isDarkMode ? 'active' : ''}`}>
        <img alt="sun" src="/static/icons/sun.svg" />
      </div>
      <div id="moon-icon" className={`moon flexed ${isDarkMode ? 'active' : ''}`}>
        <img alt="moon" src="/static/icons/moon.svg" />
      </div>
    </div>
  );
};

export const Section = ({ children, id, className = '' }: { children: React.ReactNode, id: string, className?: string }) => {
  return (
    <section id={id} className={`bg-set ${className}`}>
      {children}
    </section>
  );
};

export const Header = ({ title, className = '' }: { title: string, className?: string }) => {
  return (
    <div className={`h1 ${className}`} data-header="">
      {title}
    </div>
  );
};

export const InfoCard = ({ children, className = '' }: { children: React.ReactNode, className?: string }) => {
  return (
    <div className={`info ${className}`}>
      {children}
    </div>
  );
};
