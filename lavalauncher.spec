Name:     lavalauncher
Version:  2.0.0
Release:  1
Summary:  LavaLauncher is a simple launcher for Wayland
License:  GPLv3
URL:      https://git.sr.ht/~leon_plickat/lavalauncher
# Upstrem tag new releases but not provide release archives or tarballs, so we need clone git and tar it.
Source0:  %{name}-%{version}.tar.zst

BuildRequires:  meson
BuildRequires:  pkgconfig(cairo)
BuildRequires:  pkgconfig(scdoc)
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(wayland-cursor)
BuildRequires:  pkgconfig(wayland-egl)
BuildRequires:  pkgconfig(wayland-egl-backend)
BuildRequires:  pkgconfig(wayland-scanner)
BuildRequires:  pkgconfig(wayland-server)
BuildRequires:  pkgconfig(wayland-protocols)
BuildRequires:	pkgconfig(librsvg-2.0)

%description
LavaLauncher is a simple launcher for Wayland.

It serves a single purpose: Letting the user execute shell commands by
clicking on icons on a dynamically sized bar, placed at one of the
screen edges or in the center.

Unlike most popular launchers, LavaLauncher does not care about
.desktop files or icon themes. To create a button, you simply provide
the path to an image and a shell command. This makes LavaLauncher
considerably more flexible: You could have buttons not just for
launching applications, but also for ejecting your optical drive,
rotating your screen, sending your cat an email, playing a funny
sound, muting all audio, toggling your lamps, etc. You can turn
practically anything you could do in your shell into a button.

The configuration is done entirely via command flags. See the manpage
for details and an example.

LavaLauncher has been successfully tested with sway and wayfire.

%prep
%autosetup -p1

%build

%meson
%meson_build

%install
%meson_install

%files
%{_bindir}/%{name}
%doc README.md LICENSE
%{_mandir}/man1/%{name}.1.zst
