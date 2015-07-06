# Git hash in https://github.com/mongodb/mongo which corresponds to Version
%global mongohash 6201872043ecbbc0a4cc169b5482dcf385fc464f

Name:		mongo-tools
Version:	3.1.5
Release:	1
Summary:	MongoDB tools
License:	ASL 2.0 
URL:		https://github.com/mongodb/mongo-tools
Source0:	https://github.com/mongodb/%{name}/archive/r%{version}.tar.gz
Source10:       https://github.com/mongodb/mongo/raw/%{mongohash}/APACHE-2.0.txt

BuildRequires:	golang
BuildRequires:  openssl-devel

Conflicts:      mongodb < 3.0.0

%description
The MongoDB tools provides import, export, and diagnostic capabilities.


%prep
%setup -n %{name}-r%{version}

# Disable 
sed -i -r "s| -ldflags \"-X github.com/mongodb/mongo-tools/common/options.Gitspec \`git rev-parse HEAD\`\"||" build.sh

# Copy Apache license
cp %{SOURCE10} $(basename %{SOURCE10})

%build
./build.sh ssl

%install
install -d -m 755            %{buildroot}%{_bindir}
install -p -m 755 bin/*      %{buildroot}%{_bindir}/

%files
%doc LICENSE.md APACHE-2.0.txt README.md CONTRIBUTING.md
%{_bindir}/*

