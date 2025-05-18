import React, { useState } from 'react';
import './Home.css';
import {
  Button,
  InputField,
  FileInput,
  ResultDisplay,
  DropArea,
  FAQItem,
  Loader,
  DarkModeToggle,
  Section,
  Header,
  InfoCard
} from './components';

const Home: React.FC = () => {
  // State management
  const [isDarkMode, setIsDarkMode] = useState(false);
  const [isLoading, setIsLoading] = useState(false);
  const [navOpen, setNavOpen] = useState(false);
  const [activeTab, setActiveTab] = useState('keyGen');
  
  // Results state
  const [generatedKey, setGeneratedKey] = useState('');
  const [encryptedMessage, setEncryptedMessage] = useState('');
  const [decryptedMessage, setDecryptedMessage] = useState('');
  
  // Form states
  const [keySize, setKeySize] = useState(32);
  const [message, setMessage] = useState('');
  const [encryptionKey, setEncryptionKey] = useState('c45646a54cb2d7f4e9deaa16975cbd3d');
  const [msgToDecrypt, setMsgToDecrypt] = useState('');
  const [decryptionKey, setDecryptionKey] = useState('c45646a54cb2d7f4e9deaa16975cbd3d');
  
  // Toggle dark mode
  const toggleDarkMode = () => {
    setIsDarkMode(!isDarkMode);
    document.documentElement.classList.toggle('invert');
  };

  // Toggle mobile navigation
  const toggleNav = () => {
    setNavOpen(!navOpen);
  };

  // Scroll to section on navigation click
  const scrollToSection = (id: string) => {
    const element = document.getElementById(id);
    if (element) {
      element.scrollIntoView({ behavior: 'smooth' });
      setActiveTab(id);
    }
    setNavOpen(false);
  };

  // Handle form submissions
  const handleGenerateKey = async (e: React.FormEvent) => {
    e.preventDefault();
    setIsLoading(true);
    
    try {
      // Mock API call - replace with actual implementation
      const response = await fetch('/generate-key', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ gen_key: keySize })
      });
      
      const data = await response.json();
      setGeneratedKey(data.key);
    } catch (error) {
      console.error('Error generating key:', error);
    } finally {
      setIsLoading(false);
    }
  };

  const handleEncryptMessage = async (e: React.FormEvent) => {
    e.preventDefault();
    setIsLoading(true);
    
    try {
      // Mock API call - replace with actual implementation
      const response = await fetch('/encrypt/string', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ message, key: encryptionKey })
      });
      
      const data = await response.json();
      setEncryptedMessage(data.encrypted_message);
    } catch (error) {
      console.error('Error encrypting message:', error);
    } finally {
      setIsLoading(false);
    }
  };

  const handleDecryptMessage = async (e: React.FormEvent) => {
    e.preventDefault();
    setIsLoading(true);
    
    try {
      // Mock API call - replace with actual implementation
      const response = await fetch('/decrypt/string', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ encrypted_msg: msgToDecrypt, key: decryptionKey })
      });
      
      const data = await response.json();
      setDecryptedMessage(data.decrypted_message);
    } catch (error) {
      console.error('Error decrypting message:', error);
    } finally {
      setIsLoading(false);
    }
  };

  // Handle file uploads
  const handleEncryptFile = async (e: React.FormEvent) => {
    e.preventDefault();
    setIsLoading(true);
    
    try {
      // Mock file encryption - implement proper form submission with FormData
      // This is just a placeholder - actual implementation needed
      setTimeout(() => {
        setIsLoading(false);
        alert('File encryption would happen here.');
      }, 1000);
    } catch (error) {
      console.error('Error encrypting file:', error);
      setIsLoading(false);
    }
  };

  const handleDecryptFile = async (e: React.FormEvent) => {
    e.preventDefault();
    setIsLoading(true);
    
    try {
      // Mock file decryption - implement proper form submission with FormData
      // This is just a placeholder - actual implementation needed
      setTimeout(() => {
        setIsLoading(false);
        alert('File decryption would happen here.');
      }, 1000);
    } catch (error) {
      console.error('Error decrypting file:', error);
      setIsLoading(false);
    }
  };

  // Copy to clipboard functionality
  const copyToClipboard = (text: string) => {
    navigator.clipboard.writeText(text).then(() => {
      // Visual feedback could be added here
      alert('Copied to clipboard!');
    });
  };

  // Share website functionality
  const shareWebsite = () => {
    if (navigator.share) {
      navigator.share({
        title: 'EncryptEase - Secure Your Data',
        text: 'Check out EncryptEase for secure encryption.',
        url: window.location.href,
      });
    } else {
      copyToClipboard(window.location.href);
      alert('URL copied to clipboard!');
    }
  };

  return (
    <>
      <Loader isLoading={isLoading} />
      
      <noscript>Please Enable Javascript</noscript>
      
      {/* Header */}
      <header className="flex align-center justify-between">
        {/* Logo */}
        <div className="icon flexed">
          <img src="/static/images/logo.png" alt="logo" />
        </div>
        
        {/* Dark mode toggle + mobile nav */}
        <div className="dm ph-nav flexed f-gap-2">
          {/* Dark mode toggle */}
          <DarkModeToggle isDarkMode={isDarkMode} toggle={toggleDarkMode} />
          
          {/* Mobile navigation */}
          <div id="phNav" className="nav-phone">
            <img 
              src="/static/icons/nav.svg" 
              alt="ham" 
              id="ham" 
              className="ham" 
              onClick={toggleNav}
            />
            
            <div id="n-el" className={`nav-elements ${navOpen ? 'active' : ''}`}>
              <div className="nav-items flex-col justify-evenly">
                <div className="items flexed justify-start">
                  <a href="#keyGen" onClick={() => scrollToSection('keyGen')}>Generate Key</a>
                </div>
                <div className="items flexed justify-start">
                  <a href="#encode" onClick={() => scrollToSection('encode')}>Encrypt Message</a>
                </div>
                <div className="items flexed justify-start">
                  <a href="#encode_file" onClick={() => scrollToSection('encode_file')}>Encrypt Files</a>
                </div>
                <div className="items flexed justify-start">
                  <a href="#decode" onClick={() => scrollToSection('decode')}>Decrypt Message</a>
                </div>
                <div className="items flexed justify-start">
                  <a href="#decode_file" onClick={() => scrollToSection('decode_file')}>Decrypt Files</a>
                </div>
                <div className="items flexed justify-start">
                  <a href="#about_div" onClick={() => scrollToSection('about_div')}>About</a>
                </div>
                <div className="items flexed justify-start">
                  <a href="#contact_div" onClick={() => scrollToSection('contact_div')}>Contacts</a>
                </div>
              </div>
              
              {/* Share button */}
              <div className="share flex-col f-gap-2">
                <div className="send flexed justify-start f-gap-2" onClick={shareWebsite}>
                  <div id="share-link" className="flexed">
                    <img id="s-logo" className="flexed" src="/static/icons/share.svg" alt="" />
                  </div>
                  Share
                </div>
              </div>
            </div>
          </div>
        </div>
      </header>
      
      {/* Desktop Navigation */}
      <nav className="desktop-nav">
        <div className="nav fixed flexed">
          <div className="ul full flex-col justify-between">
            <div className={`li border flexed justify-start ${activeTab === 'keyGen' ? 'active' : ''}`}>
              <a href="#keyGen" onClick={() => scrollToSection('keyGen')}>Generate Key</a>
            </div>
            <div className={`li border flexed justify-start ${activeTab === 'encode' ? 'active' : ''}`}>
              <a href="#encode" onClick={() => scrollToSection('encode')}>Encrypt Message</a>
            </div>
            <div className={`li border flexed justify-start ${activeTab === 'encode_file' ? 'active' : ''}`}>
              <a href="#encode_file" onClick={() => scrollToSection('encode_file')}>Encrypt Files</a>
            </div>
            <div className={`li border flexed justify-start ${activeTab === 'decode' ? 'active' : ''}`}>
              <a href="#decode" onClick={() => scrollToSection('decode')}>Decrypt Message</a>
            </div>
            <div className={`li border flexed justify-start ${activeTab === 'decode_file' ? 'active' : ''}`}>
              <a href="#decode_file" onClick={() => scrollToSection('decode_file')}>Decrypt Files</a>
            </div>
            <div className={`li border flexed justify-start ${activeTab === 'about_div' ? 'active' : ''}`}>
              <a href="#about_div" onClick={() => scrollToSection('about_div')}>About</a>
            </div>
            <div className={`li border flexed justify-start ${activeTab === 'contact_div' ? 'active' : ''}`}>
              <a href="#contact_div" onClick={() => scrollToSection('contact_div')}>Contacts</a>
            </div>
          </div>
        </div>
      </nav>
      
      {/* Main Section */}
      <Section id="s1">
        <div className="s1__container full flex-col">
          {/* Heading for desktop */}
          <div className="heading flex-col desktop">
            <div className="heading1">
              <span className="scribe app_name">EncryptEase: </span>
              Secure Your Valuable Information
            </div>
            <div className="heading2">
              Effortless Encryption, That <span className="dahlia strong">ONLY YOU</span> Can Decode
            </div>
          </div>
          
          {/* Heading for mobile */}
          <div className="heading flex-col phone">
            <div className="heading1 cen">
              <span className="scribe app_name">EncryptEase</span>
            </div>
            <br />
            <div className="heading2 cen"></div>
          </div>
          
          <div className="main flex-col">
            {/* Key Generation */}
            <div id="keyGen" className="keygen forms">
              <div className="subheading flexed cen key_gen_subheading">Generate Key</div>
              <form onSubmit={handleGenerateKey}>
                <InputField
                  label="Enter Key size(16byte, 24byte or 32byte):"
                  id="gen_key"
                  name="gen_key"
                  type="number"
                  required={true}
                  min={16}
                  max={32}
                  step={8}
                  placeholder="Enter Size"
                  value={keySize.toString()}
                  onChange={(e) => setKeySize(parseInt(e.target.value))}
                />
                <Button type="submit" className="pb">Get Key</Button>
                <ResultDisplay
                  title="key:"
                  id="0"
                  content={generatedKey}
                  className="res cen flex align-center justify-start"
                />
                <Button onClick={() => copyToClipboard(generatedKey)} className="copy-btn" dataIndex="0">copy</Button>
              </form>
            </div>
            
            {/* Encrypt Message */}
            <div id="encode" className="encryption forms">
              <div className="subheading flexed cen encrypt_subheading">Encrypt Message</div>
              <form onSubmit={handleEncryptMessage}>
                <InputField
                  label="Enter Message to Encrypt:"
                  id="message"
                  name="message"
                  placeholder="Hi!"
                  required={true}
                  value={message}
                  onChange={(e) => setMessage(e.target.value)}
                  hasPaste={true}
                />
                <InputField
                  label="Enter Key:"
                  id="key"
                  name="key"
                  placeholder="Enter key"
                  value={encryptionKey}
                  onChange={(e) => setEncryptionKey(e.target.value)}
                  hasPaste={true}
                />
                <Button type="submit" className="pb">Encrypt</Button>
              </form>
              <ResultDisplay
                title="Encrypted message:"
                id="1"
                content={encryptedMessage}
              />
              <Button onClick={() => copyToClipboard(encryptedMessage)} className="copy-btn" dataIndex="1">copy</Button>
            </div>
            
            {/* Encrypt File */}
            <div id="encode_file" className="encryption forms">
              <div className="subheading flexed cen encrypt_file_subheading">Encrypt File</div>
              <form onSubmit={handleEncryptFile} encType="multipart/form-data">
                <FileInput
                  label="Choose File[size<17mb]:"
                  id="file"
                  name="file"
                  required={true}
                />
                <DropArea id="drp1" />
                <InputField
                  label="Enter Key:"
                  id="key-f-i"
                  name="key"
                  placeholder="Enter key"
                  value={encryptionKey}
                  onChange={(e) => setEncryptionKey(e.target.value)}
                  hasPaste={true}
                />
                <Button type="submit" className="pb">Encrypt</Button>
              </form>
            </div>
            
            {/* Decrypt Message */}
            <div id="decode" className="decryption forms">
              <div className="subheading flexed cen decrypt_subheading">Decrypt Message</div>
              <form onSubmit={handleDecryptMessage}>
                <InputField
                  label="Enter message to decrypt:"
                  id="encrypted_msg"
                  name="encrypted_msg"
                  placeholder="none"
                  required={true}
                  value={msgToDecrypt}
                  onChange={(e) => setMsgToDecrypt(e.target.value)}
                  hasPaste={true}
                />
                <InputField
                  label="Enter Key:"
                  id="key-ii"
                  name="key"
                  placeholder="Enter key"
                  value={decryptionKey}
                  onChange={(e) => setDecryptionKey(e.target.value)}
                  hasPaste={true}
                />
                <Button type="submit" className="pb">Decrypt</Button>
              </form>
              <ResultDisplay
                title="Decrypted message:"
                id="2"
                content={decryptedMessage}
              />
              <Button onClick={() => copyToClipboard(decryptedMessage)} className="copy-btn" dataIndex="2">copy</Button>
            </div>
            
            {/* Decrypt File */}
            <div id="decode_file" className="decryption forms">
              <div className="subheading flexed cen decrypt_file_subheading">Decrypt File</div>
              <form onSubmit={handleDecryptFile} encType="multipart/form-data">
                <FileInput
                  label="Choose File[size<17mb]:"
                  id="encrypted_file"
                  name="encrypted_file"
                  required={true}
                />
                <DropArea id="drp2" />
                <InputField
                  label="Enter Key:"
                  id="key-f-ii"
                  name="key"
                  placeholder="Enter key"
                  value={decryptionKey}
                  onChange={(e) => setDecryptionKey(e.target.value)}
                  hasPaste={true}
                />
                <Button type="submit" className="pb">Decrypt</Button>
              </form>
            </div>
          </div>
        </div>
      </Section>
      
      {/* Section 2 - About, Contact, FAQ */}
      <Section id="s2">
        <div className="s2__container full flex-col">
          {/* About */}
          <div id="about_div" className="about">
            <Header title="About" />
            <InfoCard>
              <br />
              Welcome to EncryptEase, your go-to solution for effortless data encryption and security.
              <br />
              My platform empowers you to generate secure keys, encrypt messages, and decrypt them with ease, ensuring that your sensitive information remains safe and confidential.
              <br /><br />
              Created by Subhajit Gorai, EncryptEase prioritizes user privacy and data security by not storing any user data. Feel free to use this platform as much as you need. But don't use it for any malicious purposes.
            </InfoCard>
          </div>
          
          {/* Contact */}
          <div id="contact_div" className="contact">
            <Header title="Contact" />
            <InfoCard>
              <br />
              Feel Free to contact me if needed.
              <br /><br />
              <div id="e-logo" className="email flexed f-gap-1 justify-start">
                <img src="/static/icons/email.svg" alt="email" />
                <span>Email</span>
              </div>
              <div className="icons flex-col f-gap-2 justify-start">
                <div className="github-logo flex align-center f-gap-1 p-top-05">
                  <a id="github" href="https://github.com/Dream-World-Coder" target="_blank" title="github" rel="noopener">
                    <img src="/static/icons/github.svg" alt="github" />
                  </a>
                  GitHub
                </div>
              </div>
              <div className="portfolio flexed f-gap-1 justify-start">
                <a href="https://subhajit.pages.dev" target="_blank" title="portfolio" rel="noopener">
                  <img src="/static/icons/website.svg" alt="portfolio" />
                </a>
                My Personal Website
              </div>
            </InfoCard>
          </div>
          
          {/* FAQ */}
          <div className="faq_div flex-col justify-between" id="faq_div">
            <Header title="FAQs" />
            <div className="faq_container flex-col">
              <FAQItem
                question="How to Encode?"
                answer={
                  <>
                    Provide your message or file, then generate a key of yours. Then fill up details and press
                    <code>Encrypt</code> Button. You can Encode using that.
                  </>
                }
                faqNumber="1"
              />
              
              <FAQItem
                question="How to Decode?"
                answer={
                  <>
                    Enter the Encrypted message or file and
                    <strong>provide the same key you used to encode.</strong>
                    After that you can Decode.
                  </>
                }
                faqNumber="2"
              />
              
              <FAQItem
                question="Is my encrypted data secure?"
                answer={
                  <>
                    Yes, if you generate a unique key of yours and use that for encryption,
                    <span>only you</span> can decode it.
                  </>
                }
                faqNumber="3"
              />
              
              <FAQItem
                question="Should I generate a unique key?"
                answer={
                  <>
                    Yes it's recommended to do so. But you can also encrypt using the default key, but it's not unique that way, hence not that secure.
                  </>
                }
                faqNumber="4"
              />
              
              <FAQItem
                question="How the encryption works?"
                answer={
                  <>
                    The code uses python <code>cryptography</code> module to encrypt data. And specifically it uses GCTR Mode. The cryptography module in Python allows you to encrypt text and files. It uses a secret key (like a complex password) and a random initialization vector (IV) to scramble the data with AES-256 encryption in GCTR mode. Imagine XORing your message with a random stream of bits - that's essentially what happens. This makes the data unreadable without the key. Decryption works by reversing the process with the same key and IV, making your files and messages secure.
                  </>
                }
                faqNumber="5"
              />
            </div>
          </div>
        </div>
      </Section>
    </>
  );
};

export default Home;
