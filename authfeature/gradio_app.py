import gradio as gr
from .key_manager import APIKeyManager

with gr.Blocks(title="API Key Management UI") as demo:
    gr.Markdown("# API Key Management\nMinimal Gradio UI for API Key Operations")
    with gr.Tab("Create Key"):
        create_btn = gr.Button("Create API Key")
        create_out = gr.Textbox(label="New API Key")
        def create_key():
            return APIKeyManager.create_key()
        create_btn.click(fn=create_key, outputs=create_out)
    with gr.Tab("List Keys"):
        list_btn = gr.Button("List All Keys")
        list_out = gr.Dataframe(headers=["API Keys"])
        def list_keys():
            return [[k] for k in APIKeyManager.list_keys()]
        list_btn.click(fn=list_keys, outputs=list_out)
    with gr.Tab("Usage Count"):
        key_in = gr.Textbox(label="API Key")
        usage_btn = gr.Button("Get Usage Count")
        usage_out = gr.Number(label="Usage Count")
        def get_usage(key):
            return APIKeyManager.get_usage(key)
        usage_btn.click(fn=get_usage, inputs=key_in, outputs=usage_out)
    with gr.Tab("Increment Usage"):
        inc_key_in = gr.Textbox(label="API Key")
        inc_btn = gr.Button("Increment Usage")
        inc_out = gr.Number(label="New Usage Count")
        def inc_usage(key):
            return APIKeyManager.increment_usage(key)
        inc_btn.click(fn=inc_usage, inputs=inc_key_in, outputs=inc_out)
    with gr.Tab("Revoke/Delete Key"):
        del_key_in = gr.Textbox(label="API Key")
        del_btn = gr.Button("Delete Key")
        del_out = gr.Textbox(label="Status")
        def delete_key(key):
            return "deleted" if APIKeyManager.delete_key(key) else "not found"
        del_btn.click(fn=delete_key, inputs=del_key_in, outputs=del_out)

def launch():
    demo.launch()

if __name__ == "__main__":
    launch()
