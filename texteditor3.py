import flet as ft
 
def main(page: ft.Page):
    page.title = "Text Editor"
 
    word_result = ft.Text("Words: 0", size=40)
    characthers_results = ft.Text("Characters: 0", size=40)
 
    def update_counts(e):
        text = mainTf.value
 
        countletters = len(text)
        word_count = len(text.split())
 
 
        word_result.value = f"Words: {word_count}"
        characthers_results.value = f"Characters: {countletters}"
 
        page.update()
 
    def clear_text(e):
        mainTf.value = ""
        word_result = "Words: 0"
        characthers_results = "Characters: 0"
        page.update()
 
    mainTf = ft.TextField(
        multiline = True,
        expand = True,
        hint_text = "Write the text you want here",
        on_change =update_counts
 
    )
    
 
 
    clearButton = ft.ElevatedButton(
        "Clear",
        on_click = clear_text
    )
 
    page.add(
        mainTf,
        ft.Row([word_result, characthers_results, clearButton])
    )
 
ft.run(main=main)