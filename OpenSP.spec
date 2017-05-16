#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : OpenSP
Version  : 1.5.2
Release  : 14
URL      : https://sourceforge.net/projects/openjade/files/opensp/1.5.2/OpenSP-1.5.2.tar.gz
Source0  : https://sourceforge.net/projects/openjade/files/opensp/1.5.2/OpenSP-1.5.2.tar.gz
Summary  : The OpenJade Group's SGML and XML parsing tools
Group    : Development/Tools
License  : MIT
Requires: OpenSP-bin
Requires: OpenSP-lib
Requires: OpenSP-data
Requires: OpenSP-doc
Requires: OpenSP-locales
BuildRequires : bison
BuildRequires : libxslt-bin
BuildRequires : util-linux

%description
This package is a collection of SGML/XML tools called OpenSP. It is a fork from
James Clark's SP suite. These tools are used to parse, validate, and normalize
SGML and XML files.

%package bin
Summary: bin components for the OpenSP package.
Group: Binaries
Requires: OpenSP-data

%description bin
bin components for the OpenSP package.


%package data
Summary: data components for the OpenSP package.
Group: Data

%description data
data components for the OpenSP package.


%package dev
Summary: dev components for the OpenSP package.
Group: Development
Requires: OpenSP-lib
Requires: OpenSP-bin
Requires: OpenSP-data
Provides: OpenSP-devel

%description dev
dev components for the OpenSP package.


%package doc
Summary: doc components for the OpenSP package.
Group: Documentation

%description doc
doc components for the OpenSP package.


%package lib
Summary: lib components for the OpenSP package.
Group: Libraries
Requires: OpenSP-data

%description lib
lib components for the OpenSP package.


%package locales
Summary: locales components for the OpenSP package.
Group: Default

%description locales
locales components for the OpenSP package.


%prep
%setup -q -n OpenSP-1.5.2

%build
export LANG=C
export SOURCE_DATE_EPOCH=1489101618
%configure --disable-static --disable-doc-build
make V=1  %{?_smp_mflags}

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost
make VERBOSE=1 V=1 %{?_smp_mflags} check || :

%install
export SOURCE_DATE_EPOCH=1489101618
rm -rf %{buildroot}
%make_install
%find_lang sp5

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/onsgmls
/usr/bin/osgmlnorm
/usr/bin/ospam
/usr/bin/ospcat
/usr/bin/ospent
/usr/bin/osx

%files data
%defattr(-,root,root,-)
/usr/share/OpenSP/HTML32.dcl
/usr/share/OpenSP/HTML32.dtd
/usr/share/OpenSP/HTML32.soc
/usr/share/OpenSP/HTML4-f.dtd
/usr/share/OpenSP/HTML4-s.dtd
/usr/share/OpenSP/HTML4.dcl
/usr/share/OpenSP/HTML4.dtd
/usr/share/OpenSP/HTML4.soc
/usr/share/OpenSP/HTMLlat1.ent
/usr/share/OpenSP/HTMLspec.ent
/usr/share/OpenSP/HTMLsym.ent
/usr/share/OpenSP/ISOlat1.ent
/usr/share/OpenSP/ISOlat1.sgm
/usr/share/OpenSP/catalog
/usr/share/OpenSP/demo.sgm
/usr/share/OpenSP/gensyntax.pl
/usr/share/OpenSP/html-1.dtd
/usr/share/OpenSP/html-1s.dtd
/usr/share/OpenSP/html-s.dtd
/usr/share/OpenSP/html.dcl
/usr/share/OpenSP/html.dtd
/usr/share/OpenSP/html.soc
/usr/share/OpenSP/japan.dcl
/usr/share/OpenSP/opensp-implied.dcl
/usr/share/OpenSP/unicode.sd
/usr/share/OpenSP/unicode.syn
/usr/share/OpenSP/xml.dcl
/usr/share/OpenSP/xml.soc

%files dev
%defattr(-,root,root,-)
/usr/include/OpenSP/Allocator.h
/usr/include/OpenSP/ArcEngine.h
/usr/include/OpenSP/Attribute.h
/usr/include/OpenSP/Attributed.h
/usr/include/OpenSP/Big5CodingSystem.h
/usr/include/OpenSP/Boolean.h
/usr/include/OpenSP/CharMap.cxx
/usr/include/OpenSP/CharMap.h
/usr/include/OpenSP/CharsetDecl.h
/usr/include/OpenSP/CharsetInfo.h
/usr/include/OpenSP/CharsetRegistry.h
/usr/include/OpenSP/CmdLineApp.h
/usr/include/OpenSP/CodingSystem.h
/usr/include/OpenSP/CodingSystemKit.h
/usr/include/OpenSP/ConsoleOutput.h
/usr/include/OpenSP/ContentState.h
/usr/include/OpenSP/ContentToken.h
/usr/include/OpenSP/CopyOwner.cxx
/usr/include/OpenSP/CopyOwner.h
/usr/include/OpenSP/DescriptorManager.h
/usr/include/OpenSP/Dtd.h
/usr/include/OpenSP/EUCJPCodingSystem.h
/usr/include/OpenSP/ElementType.h
/usr/include/OpenSP/Entity.h
/usr/include/OpenSP/EntityApp.h
/usr/include/OpenSP/EntityCatalog.h
/usr/include/OpenSP/EntityDecl.h
/usr/include/OpenSP/EntityManager.h
/usr/include/OpenSP/ErrnoMessageArg.h
/usr/include/OpenSP/ErrorCountEventHandler.h
/usr/include/OpenSP/Event.h
/usr/include/OpenSP/EventGenerator.h
/usr/include/OpenSP/EventsWanted.h
/usr/include/OpenSP/ExtendEntityManager.h
/usr/include/OpenSP/ExternalId.h
/usr/include/OpenSP/Fixed2CodingSystem.h
/usr/include/OpenSP/Fixed4CodingSystem.h
/usr/include/OpenSP/GenericEventHandler.h
/usr/include/OpenSP/Hash.h
/usr/include/OpenSP/HashTable.cxx
/usr/include/OpenSP/HashTable.h
/usr/include/OpenSP/HashTableItemBase.cxx
/usr/include/OpenSP/HashTableItemBase.h
/usr/include/OpenSP/IList.h
/usr/include/OpenSP/IListBase.h
/usr/include/OpenSP/IListIter.h
/usr/include/OpenSP/IListIterBase.h
/usr/include/OpenSP/IQueue.cxx
/usr/include/OpenSP/IQueue.h
/usr/include/OpenSP/ISet.cxx
/usr/include/OpenSP/ISet.h
/usr/include/OpenSP/ISetIter.h
/usr/include/OpenSP/IdentityCodingSystem.h
/usr/include/OpenSP/InputSource.h
/usr/include/OpenSP/InternalInputSource.h
/usr/include/OpenSP/Link.h
/usr/include/OpenSP/LinkProcess.h
/usr/include/OpenSP/List.cxx
/usr/include/OpenSP/List.h
/usr/include/OpenSP/ListIter.h
/usr/include/OpenSP/LiteralStorage.h
/usr/include/OpenSP/Location.h
/usr/include/OpenSP/Lpd.h
/usr/include/OpenSP/Markup.h
/usr/include/OpenSP/Message.h
/usr/include/OpenSP/MessageArg.h
/usr/include/OpenSP/MessageBuilder.h
/usr/include/OpenSP/MessageEventHandler.h
/usr/include/OpenSP/MessageFormatter.h
/usr/include/OpenSP/MessageModule.h
/usr/include/OpenSP/MessageReporter.h
/usr/include/OpenSP/MessageTable.h
/usr/include/OpenSP/Mode.h
/usr/include/OpenSP/NCVector.h
/usr/include/OpenSP/Named.h
/usr/include/OpenSP/NamedResource.h
/usr/include/OpenSP/NamedResourceTable.h
/usr/include/OpenSP/NamedTable.h
/usr/include/OpenSP/Notation.h
/usr/include/OpenSP/NotationStorage.h
/usr/include/OpenSP/OpenElement.h
/usr/include/OpenSP/Options.cxx
/usr/include/OpenSP/Options.h
/usr/include/OpenSP/OutputByteStream.h
/usr/include/OpenSP/OutputCharStream.h
/usr/include/OpenSP/Owner.cxx
/usr/include/OpenSP/Owner.h
/usr/include/OpenSP/OwnerTable.cxx
/usr/include/OpenSP/OwnerTable.h
/usr/include/OpenSP/ParserApp.h
/usr/include/OpenSP/ParserEventGeneratorKit.h
/usr/include/OpenSP/ParserOptions.h
/usr/include/OpenSP/PointerTable.cxx
/usr/include/OpenSP/PointerTable.h
/usr/include/OpenSP/PosixStorage.h
/usr/include/OpenSP/Ptr.cxx
/usr/include/OpenSP/Ptr.h
/usr/include/OpenSP/RangeMap.cxx
/usr/include/OpenSP/RangeMap.h
/usr/include/OpenSP/Resource.h
/usr/include/OpenSP/RewindStorageObject.h
/usr/include/OpenSP/SGMLApplication.h
/usr/include/OpenSP/SJISCodingSystem.h
/usr/include/OpenSP/SOEntityCatalog.h
/usr/include/OpenSP/Sd.h
/usr/include/OpenSP/SdText.h
/usr/include/OpenSP/SearchResultMessageArg.h
/usr/include/OpenSP/SgmlParser.h
/usr/include/OpenSP/ShortReferenceMap.h
/usr/include/OpenSP/StdioStorage.h
/usr/include/OpenSP/StorageManager.h
/usr/include/OpenSP/StringC.h
/usr/include/OpenSP/StringOf.cxx
/usr/include/OpenSP/StringOf.h
/usr/include/OpenSP/StringResource.h
/usr/include/OpenSP/SubstTable.h
/usr/include/OpenSP/Syntax.h
/usr/include/OpenSP/Text.h
/usr/include/OpenSP/TranslateCodingSystem.h
/usr/include/OpenSP/TypeId.h
/usr/include/OpenSP/URLStorage.h
/usr/include/OpenSP/UTF16CodingSystem.h
/usr/include/OpenSP/UTF8CodingSystem.h
/usr/include/OpenSP/UnicodeCodingSystem.h
/usr/include/OpenSP/UnivCharsetDesc.h
/usr/include/OpenSP/Vector.cxx
/usr/include/OpenSP/Vector.h
/usr/include/OpenSP/XMLCodingSystem.h
/usr/include/OpenSP/XcharMap.cxx
/usr/include/OpenSP/XcharMap.h
/usr/include/OpenSP/config.h
/usr/include/OpenSP/constant.h
/usr/include/OpenSP/macros.h
/usr/include/OpenSP/rtti.h
/usr/include/OpenSP/sptchar.h
/usr/include/OpenSP/types.h
/usr/include/OpenSP/xnew.h
/usr/lib64/libosp.so

%files doc
%defattr(-,root,root,-)
%doc /usr/share/doc/OpenSP/*

%files lib
%defattr(-,root,root,-)
/usr/lib64/libosp.so.5
/usr/lib64/libosp.so.5.0.0

%files locales -f sp5.lang
%defattr(-,root,root,-)

