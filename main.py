import flet as ft
import zipfile
import os
import json

def main(page: ft.Page):
    page.title = "PassThm Creator"
    page.theme_mode = ft.ThemeMode.DARK
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    
    status_text = ft.Text(value="Готов к работе", color="green")
    
    def build_theme(e):
        # Логика сборки .passthm
        theme_dir = "/tmp/my_theme" # В реальном приложении используем временные папки iOS
        os.makedirs(theme_dir, exist_ok=True)
        
        # Создаем манифест темы
        manifest = {
            "name": "My Custom Pass",
            "author": "Developer",
            "version": "1.0"
        }
        
        with open(os.path.join(theme_dir, "theme.json"), "w") as f:
            json.dump(manifest, f)
            
        # Упаковываем в .passthm (тот же zip)
        output_path = "/tmp/theme.passthm"
        with zipfile.ZipFile(output_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
            zipf.write(os.path.join(theme_dir, "theme.json"), "theme.json")
            # Здесь также добавляются картинки keypad-0.png и т.д.
            
        status_text.value = f"Тема успешно создана: {output_path}"
        page.update()

    # Интерфейс приложения
    page.add(
        ft.Center(
            ft.Column([
                ft.Text("Генератор тем для экрана пароля iOS", size=20, weight=ft.FontWeight.BOLD),
                ft.ElevatedButton("Собрать .passthm", on_click=build_theme),
                status_text
            ], horizontal_alignment=ft.CrossAxisAlignment.CENTER)
        )
    )

ft.app(target=main)
