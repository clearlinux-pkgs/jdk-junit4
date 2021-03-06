#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : jdk-junit4
Version  : 4.12
Release  : 7
URL      : https://github.com/junit-team/junit4/archive/r4.12.tar.gz
Source0  : https://github.com/junit-team/junit4/archive/r4.12.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : EPL-1.0
Requires: jdk-junit4-data
BuildRequires : apache-maven
BuildRequires : apache-maven2
BuildRequires : javapackages-tools
BuildRequires : jdk-aether
BuildRequires : jdk-aopalliance
BuildRequires : jdk-apache-parent
BuildRequires : jdk-aqute-bndlib
BuildRequires : jdk-atinject
BuildRequires : jdk-bsh
BuildRequires : jdk-cdi-api
BuildRequires : jdk-commons-beanutils
BuildRequires : jdk-commons-cli
BuildRequires : jdk-commons-codec
BuildRequires : jdk-commons-collections
BuildRequires : jdk-commons-compress
BuildRequires : jdk-commons-digester
BuildRequires : jdk-commons-io
BuildRequires : jdk-commons-lang
BuildRequires : jdk-commons-lang3
BuildRequires : jdk-commons-logging
BuildRequires : jdk-commons-validator
BuildRequires : jdk-doxia
BuildRequires : jdk-doxia-sitetools
BuildRequires : jdk-eclipse-eclipse
BuildRequires : jdk-eclipse-osgi
BuildRequires : jdk-eclipse-osgi-services
BuildRequires : jdk-enforcer
BuildRequires : jdk-felix
BuildRequires : jdk-felix-bundlerepository
BuildRequires : jdk-felix-framework
BuildRequires : jdk-felix-osgi-foundation
BuildRequires : jdk-felix-utils
BuildRequires : jdk-glassfish-servlet-api
BuildRequires : jdk-guava
BuildRequires : jdk-guice
BuildRequires : jdk-hamcrest
BuildRequires : jdk-httpcomponents-client
BuildRequires : jdk-httpcomponents-core
BuildRequires : jdk-jsoup
BuildRequires : jdk-jsr-305
BuildRequires : jdk-kxml
BuildRequires : jdk-log4j
BuildRequires : jdk-maven-archiver
BuildRequires : jdk-maven-bundle-plugin
BuildRequires : jdk-maven-common-artifact-filters
BuildRequires : jdk-maven-compiler-plugin
BuildRequires : jdk-maven-dependency-tree
BuildRequires : jdk-maven-filtering
BuildRequires : jdk-maven-invoker
BuildRequires : jdk-maven-javadoc-plugin
BuildRequires : jdk-maven-plugin-testing
BuildRequires : jdk-maven-plugin-tools
BuildRequires : jdk-maven-reporting-api
BuildRequires : jdk-maven-reporting-impl
BuildRequires : jdk-maven-resources-plugin
BuildRequires : jdk-maven-shared-incremental
BuildRequires : jdk-maven-shared-utils
BuildRequires : jdk-objectweb-asm
BuildRequires : jdk-osgi-compendium
BuildRequires : jdk-osgi-core
BuildRequires : jdk-plexus-archiver
BuildRequires : jdk-plexus-build-api
BuildRequires : jdk-plexus-cipher
BuildRequires : jdk-plexus-classworlds
BuildRequires : jdk-plexus-compiler
BuildRequires : jdk-plexus-containers
BuildRequires : jdk-plexus-i18n
BuildRequires : jdk-plexus-interactivity
BuildRequires : jdk-plexus-interpolation
BuildRequires : jdk-plexus-io
BuildRequires : jdk-plexus-sec-dispatcher
BuildRequires : jdk-plexus-utils
BuildRequires : jdk-plexus-velocity
BuildRequires : jdk-sisu
BuildRequires : jdk-slf4j
BuildRequires : jdk-snappy-java
BuildRequires : jdk-surefire
BuildRequires : jdk-velocity
BuildRequires : jdk-wagon
BuildRequires : jdk-xbean
BuildRequires : jdk-xmlunit
BuildRequires : lxml
BuildRequires : openjdk-dev
BuildRequires : python3
BuildRequires : six
BuildRequires : xmvn

%description
# JUnit 4
JUnit is a simple framework to write repeatable tests. It is an instance of the xUnit architecture for unit testing frameworks.

%package data
Summary: data components for the jdk-junit4 package.
Group: Data

%description data
data components for the jdk-junit4 package.


%prep
%setup -q -n junit4-r4.12

sed -i /InaccessibleBaseClassTest/d src/test/java/org/junit/tests/AllTests.java
python3 /usr/share/java-utils/pom_editor.py pom_remove_plugin  :replacer
sed s/@version@/4.12/ src/main/java/junit/runner/Version.java.template >src/main/java/junit/runner/Version.java
python3 /usr/share/java-utils/pom_editor.py pom_remove_plugin  :animal-sniffer-maven-plugin
python3 /usr/share/java-utils/pom_editor.py pom_remove_plugin  :maven-javadoc-plugin
python3 /usr/share/java-utils/pom_editor.py pom_xpath_inject   pom:project "<packaging>bundle</packaging>"
python3 /usr/share/java-utils/pom_editor.py pom_xpath_inject   pom:build/pom:plugins "
<plugin>
<groupId>org.apache.felix</groupId>
<artifactId>maven-bundle-plugin</artifactId>
<extensions>true</extensions>
<configuration>
<instructions>
<Bundle-SymbolicName>org.junit</Bundle-SymbolicName>
<Export-Package>{local-packages},!org.hamcrest*,*;x-internal:=true</Export-Package>
<_nouses>true</_nouses>
</instructions>
</configuration>
</plugin>"
python3 /usr/share/java-utils/mvn_file.py : junit

%build
python3 /usr/share/java-utils/mvn_build.py

%install
xmvn-install  -R .xmvn-reactor -n junit -d %{buildroot}

%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/java/junit.jar
/usr/share/maven-metadata/junit.xml
/usr/share/maven-poms/junit.pom
