import json
import os
from datetime import datetime


class Note:
    def __init__(self, note_id, title, body, created_at, updated_at):
        self.note_id = note_id
        self.title = title
        self.body = body
        self.created_at = created_at
        self.updated_at = updated_at


class NotesManager:
    def __init__(self):
        self.notes = []
        self.file_path = 'notes.json'

        # Load existing notes from file
        if os.path.exists(self.file_path):
            with open(self.file_path, 'r') as file:
                notes_data = json.load(file)
                for note_data in notes_data:
                    note = Note(
                        note_data['note_id'],
                        note_data['title'],
                        note_data['body'],
                        note_data['created_at'],
                        note_data['updated_at']
                    )
                    self.notes.append(note)

    def save_notes(self):
        notes_data = []
        for note in self.notes:
            note_data = {
                'note_id': note.note_id,
                'title': note.title,
                'body': note.body,
                'created_at': note.created_at,
                'updated_at': note.updated_at
            }
            notes_data.append(note_data)

        with open(self.file_path, 'w') as file:
            json.dump(notes_data, file, indent=4)

    def create_note(self, title, body):
        note_id = len(self.notes) + 1
        created_at = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        updated_at = created_at

        note = Note(note_id, title, body, created_at, updated_at)
        self.notes.append(note)
        self.save_notes()

        print('Note created successfully.')

    def read_notes(self):
        if not self.notes:
            print('No notes found.')
            return

        print('--- Notes ---')
        for note in self.notes:
            print(f'ID: {note.note_id}')
            print(f'Title: {note.title}')
            print(f'Body: {note.body}')
            print(f'Created At: {note.created_at}')
            print(f'Updated At: {note.updated_at}')
            print('---------------')

    def edit_note(self, note_id, title, body):
        for note in self.notes:
            if note.note_id == note_id:
                note.title = title
                note.body = body
                note.updated_at = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                self.save_notes()
                print('Note updated successfully.')
                return

        print('Note not found.')

    def delete_note(self, note_id):
        for note in self.notes:
            if note.note_id == note_id:
                self.notes.remove(note)
                self.save_notes()
                print('Note deleted successfully.')
                return

        print('Note not found.')


def main():
    notes_manager = NotesManager()

    while True:
        print('--- Menu ---')
        print('1. Create a note')
        print('2. Read notes')
        print('3. Edit a note')
        print('4. Delete a note')
        print('5. Exit')

        choice = input('Enter your choice: ')

        if choice == '1':
            title = input('Enter the note title: ')
            body = input('Enter the note body: ')
            notes_manager.create_note(title, body)
        elif choice == '2':
            notes_manager.read_notes()
        elif choice == '3':
            note_id = int(input('Enter the ID of the note to edit: '))
            title = input('Enter the updated note title: ')
            body = input('Enter the updated note body: ')
            notes_manager.edit_note(note_id, title, body)
        elif choice == '4':
            note_id = int(input('Enter the ID of the note to delete: '))
            notes_manager.delete_note(note_id)
        elif choice == '5':
            break
        else:
            print('Invalid choice. Please try again.')


if __name__ == '__main__':
    main()
