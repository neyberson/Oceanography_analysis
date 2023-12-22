def plot_currents(u, v, lat, lon):

    # Create a figure and axes.
    fig, ax = plt.subplots()

    # Plot the currents.
    ax.quiver(lon, lat, u, v)

    # Add a colorbar.
    cb = plt.colorbar()
    cb.set_label('Current speed (m/s)')

    # Add a title.
    plt.title('Currents')

    # Show the plot.
    plt.show()
    
    
    
u = np.loadtxt('u.txt')
v = np.loadtxt('v.txt')
lat = np.loadtxt('lat.txt')
lon = np.loadtxt('lon.txt')

plot_currents(u, v, lat, lon)