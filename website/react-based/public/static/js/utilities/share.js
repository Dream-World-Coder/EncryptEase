document.addEventListener('DOMContentLoaded', () => {
  const shareButton = document.getElementById('share-link');

  shareButton.addEventListener('click', async () => {
    if (navigator.share) {
      try {
        await navigator.share({
          title: document.title,
          text: 'Check out this awesome website!',
          url: window.location.href
        });
        console.log('Content shared successfully');
      } catch (error) {
        console.error('Error sharing content:', error);
      }
    } else {
      // Fallback for browsers that do not support the Web Share API
      copyToClipboard(window.location.href);
      alert('Link copied to clipboard: ' + window.location.href);
    }
  });

  function copyToClipboard(text) {
    const textarea = document.createElement('textarea');
    textarea.value = text;
    document.body.appendChild(textarea);
    textarea.select();
    document.execCommand('copy');
    document.body.removeChild(textarea);
  }
});
