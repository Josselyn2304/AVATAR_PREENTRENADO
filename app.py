import gradio as gr

class AvatarApp:
    def __init__(self):
        pass

    def generate_avatar(self, style):
        # Placeholder for avatar generation logic
        return f"Generated a {style} avatar!"

def create_interface():
    app = AvatarApp()
    styles = ['Cartoon', 'Realistic', '3D Pixar']
    iface = gr.Interface(
        fn=app.generate_avatar,
        inputs=gr.inputs.Radio(choices=styles, label="Select Avatar Style"),
        outputs="text",
        title="3D Pixar-style Avatar Generator",
        description="Generate your own 3D Pixar-style avatar with various style controls."
    )
    return iface

if __name__ == '__main__':
    create_interface().launch()