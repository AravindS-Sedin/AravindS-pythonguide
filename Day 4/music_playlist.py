# Music Playlist using Doubly Linked List
#
# Features:
# 1. Add songs to playlist.
# 2. Play next/previous song.
# 3. Remove currently playing song.
# 4. Display playlist with currently playing marker.
# 5. Duration shown in mm:ss format.


class SongNode:

    def __init__(self, name, artist, duration):
        self.name = name
        self.artist = artist
        self.duration = duration

        self.prev = None
        self.next = None


class Playlist:

    def __init__(self):
        self.head = None
        self.tail = None
        self.current = None

    def add_song(self, name, artist, duration):

        new_song = SongNode(name, artist, duration)

        if self.head is None:
            self.head = self.tail = self.current = new_song
            return

        self.tail.next = new_song
        new_song.prev = self.tail
        self.tail = new_song

    def next_track(self):

        if self.current is None:
            print("Playlist is empty")
            return

        if self.current.next is None:
            print("End of playlist")
            return

        self.current = self.current.next

        print(
            f"Now playing: "
            f"{self.current.name} — {self.current.artist}"
        )

    def prev_track(self):

        if self.current is None:
            print("Playlist is empty")
            return

        if self.current.prev is None:
            print("Already at beginning")
            return

        self.current = self.current.prev

        print(
            f"Now playing: "
            f"{self.current.name} — {self.current.artist}"
        )

    def remove_current(self):

        if self.current is None:
            print("Playlist is empty")
            return

        removed_song = self.current

        print(f"Removed: {removed_song.name}")

        # Only one song
        if self.head == self.tail:
            self.head = self.tail = self.current = None
            return

        # First song
        if removed_song == self.head:

            self.head = removed_song.next
            self.head.prev = None

            self.current = self.head
            return

        # Last song
        if removed_song == self.tail:

            self.tail = removed_song.prev
            self.tail.next = None

            self.current = self.tail
            return

        # Middle song
        prev_node = removed_song.prev
        next_node = removed_song.next

        prev_node.next = next_node
        next_node.prev = prev_node

        self.current = next_node

    def show_queue(self):

        if self.head is None:
            print("Playlist is empty")
            return

        print("\nQueue:\n")

        temp = self.head
        count = 1

        while temp:

            minutes = temp.duration // 60
            seconds = temp.duration % 60

            marker = ""

            if temp == self.current:
                marker = " [playing]"

            print(
                f"{count}. "
                f"{temp.name} — {temp.artist} "
                f"({minutes}:{seconds:02d})"
                f"{marker}"
            )

            temp = temp.next
            count += 1


playlist = Playlist()

playlist.add_song("Kesariya", "Arijit", 262)
playlist.add_song("Raataan", "Jubin", 218)
playlist.add_song("Tum Hi Ho", "Arijit", 261)
playlist.add_song("Believer", "Imagine Dragons", 204)

playlist.next_track()
playlist.next_track()

playlist.remove_current()

playlist.show_queue()