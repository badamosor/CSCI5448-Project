import observer, Playlist, User

class CollaborativePlaylist (observer.Subject, Playlist.Playlist):
    pass

if __name__ == '__main__':
    pl = CollaborativePlaylist()
    user = User.User()
    user.setName("Bada")
    print (user.getName())


    pl.attach(user)
    pl.notify()
