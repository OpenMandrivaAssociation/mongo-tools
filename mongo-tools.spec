# Git hash in https://github.com/mongodb/mongo which corresponds to Version
%global mongohash 6201872043ecbbc0a4cc169b5482dcf385fc464f

Name:		mongo-tools
Version:	3.0.3
Release:	1%{?dist}
Summary:	MongoDB tools
License:	ASL 2.0 
URL:		https://github.com/mongodb/mongo-tools
Source0:	https://github.com/mongodb/%{name}/archive/r%{version}.tar.gz
# Mongo-tools does not contain man files yet
# - see https://groups.google.com/forum/#!topic/mongodb-dev/t6Sd2Bki12I
Source1:        https://github.com/mongodb/mongo/raw/%{mongohash}/debian/bsondump.1
Source2:        https://github.com/mongodb/mongo/raw/%{mongohash}/debian/mongodump.1
Source3:        https://github.com/mongodb/mongo/raw/%{mongohash}/debian/mongoexport.1
Source4:        https://github.com/mongodb/mongo/raw/%{mongohash}/debian/mongofiles.1
Source5:        https://github.com/mongodb/mongo/raw/%{mongohash}/debian/mongoimport.1
Source6:        https://github.com/mongodb/mongo/raw/%{mongohash}/debian/mongooplog.1
Source7:        https://github.com/mongodb/mongo/raw/%{mongohash}/debian/mongorestore.1
Source8:        https://github.com/mongodb/mongo/raw/%{mongohash}/debian/mongostat.1
Source9:        https://github.com/mongodb/mongo/raw/%{mongohash}/debian/mongotop.1
Source10:       https://github.com/mongodb/mongo/raw/%{mongohash}/APACHE-2.0.txt

BuildRequires:	golang
BuildRequires:  openssl-devel

Conflicts:      mongodb < 3.0.0

%description
The MongoDB tools provides import, export, and diagnostic capabilities.


%prep
%autosetup -n %{name}-r%{version}

# Disable 
sed -i -r "s| -ldflags \"-X github.com/mongodb/mongo-tools/common/options.Gitspec \`git rev-parse HEAD\`\"||" build.sh

# Copy Apache license
cp %{SOURCE10} $(basename %{SOURCE10})

%build
./build.sh ssl

%install
install -d -m 755            %{buildroot}%{_bindir}
install -p -m 755 bin/*      %{buildroot}%{_bindir}/

install -d -m 755            %{buildroot}%{_mandir}/man1
install -p -m 644 %{SOURCE1} %{buildroot}%{_mandir}/man1/
install -p -m 644 %{SOURCE2} %{buildroot}%{_mandir}/man1/
install -p -m 644 %{SOURCE3} %{buildroot}%{_mandir}/man1/
install -p -m 644 %{SOURCE4} %{buildroot}%{_mandir}/man1/
install -p -m 644 %{SOURCE5} %{buildroot}%{_mandir}/man1/
install -p -m 644 %{SOURCE6} %{buildroot}%{_mandir}/man1/
install -p -m 644 %{SOURCE7} %{buildroot}%{_mandir}/man1/
install -p -m 644 %{SOURCE8} %{buildroot}%{_mandir}/man1/
install -p -m 644 %{SOURCE9} %{buildroot}%{_mandir}/man1/


%files
%license LICENSE.md APACHE-2.0.txt
%doc README.md CONTRIBUTING.md
%{_bindir}/*
%{_mandir}/man1/*

%changelog
* Mon May 11 2015 Marek Skalicky <mskalick@redhat.com> - 3.0.3-1
- Upgrade to version 3.0.3
- Add Apache license

* Mon May 4 2015 Marek Skalicky <mskalick@redhat.com> - 3.0.2-1
- Initial packaging
