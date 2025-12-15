from PIL import Image, ImageDraw

def create_circular_favicon(input_path, output_path, size=(64, 64)):
    try:
        # Open the image
        img = Image.open(input_path).convert("RGBA")
        
        # Calculate dimensions for a square crop
        width, height = img.size
        min_dim = min(width, height)
        
        # Center crop
        left = (width - min_dim) / 2
        top = (height - min_dim) / 2
        right = (width + min_dim) / 2
        bottom = (height + min_dim) / 2
        
        img = img.crop((left, top, right, bottom))
        
        # Resize to desired favicon size (using LANCZOS for high quality downsampling)
        img = img.resize(size, Image.Resampling.LANCZOS)
        
        # Create a circular mask
        mask = Image.new('L', size, 0)
        draw = ImageDraw.Draw(mask)
        draw.ellipse((0, 0) + size, fill=255)
        
        # Apply the mask
        output = Image.new('RGBA', size, (0, 0, 0, 0))
        output.paste(img, (0, 0), mask)
        
        # Save as PNG (favicon.png is widely supported)
        output.save(output_path, format="PNG")
        print(f"Successfully created {output_path}")
        
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    create_circular_favicon("fix-avatar.jpg", "favicon.png")
