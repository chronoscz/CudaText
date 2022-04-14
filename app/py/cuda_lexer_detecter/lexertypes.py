TYPES = {
    "/.htaccess": ['Apache config'],
    "/.htpasswd": ['Apache config'],
    "/.env": ['DotENV'],
    "/.env.dist": ['DotENV'],
    "/.env.local": ['DotENV'],
    "/.env.sample": ['DotENV'],
    "/.env.example": ['DotENV'],
    "/.env.test": ['DotENV'],
    "/.env.test.local": ['DotENV'],
    "/.env.testing": ['DotENV'],
    "/.env.dev": ['DotENV'],
    "/.env.development": ['DotENV'],
    "/.env.development.local": ['DotENV'],
    "/.env.prod": ['DotENV'],
    "/.env.production": ['DotENV'],
    "/.env.production.local": ['DotENV'],
    "/.env.dusk.local": ['DotENV'],
    "/.env.staging": ['DotENV'],
    "/.env.default": ['DotENV'],
    "/.env.defaults": ['DotENV'],
    "/.envrc": ['DotENV'],
    "/.flaskenv": ['DotENV'],
    "/Dockerfile": ['Dockerfile'],
    "/PKGBUILD": ['PKGBUILD'],
    "/config.nims": ['Nim'],
    "/configure.ac": ['Autoconf M4'],
    "/configure.in": ['Autoconf M4'],
    "/fluentd.conf": ['Apache config'],
    "/hosts": ['Properties'],
    "/httpd.conf": ['Apache config'],
    "/Jamfile": ['Perforce Jam'],
    "/logstash.conf": ['Logstash DSL'],
    "/logstash.conf.j2": ['Logstash DSL'],
    "/logstash.conf.template": ['Logstash DSL'],
    "/makefile": ['Makefile'],
    "/makefile.bcc": ['Makefile'],
    "/makefile.bor": ['Makefile'],
    "/makefile.dm": ['Makefile'],
    "/makefile.fpc": ['Makefile'],
    "/makefile.gcc": ['Makefile'],
    "/makefile.gnu": ['Makefile'],
    "/makefile.msc": ['Makefile'],
    "/makefile.vc": ['Makefile'],
    "/meson.build": ['Meson'],
    "/meson_options.txt": ['Meson'],
    "/nginx.conf": ['Nginx'],
    "/singularity": ['Singularity'],
    "4gl": ['Informix 4GL'],
    "Appfile": ['Ruby'],
    "Appraisals": ['Ruby'],
    "Berksfile": ['Ruby'],
    "Brewfile": ['Ruby'],
    "Cakefile": ['CoffeeScript'],
    "Cheffile": ['Ruby'],
    "Deliverfile": ['Ruby'],
    "Fastfile": ['Ruby'],
    "Gemfile": ['Ruby'],
    "Guardfile": ['Ruby'],
    "Lola": ['Lola-2'],
    "Podfile": ['Ruby'],
    "Rakefile": ['Ruby'],
    "Rantfile": ['Ruby'],
    "Rmd": ['R Markdown'],
    "S": ['Assembly ARM', 'Assembly GNU AS', 'Assembly RISC-V'],
    "Scanfile": ['Ruby'],
    "Snapfile": ['Ruby'],
    "Thorfile": ['Ruby'],
    "Vagrantfile": ['Ruby'],
    "_coffee": ['CoffeeScript'],
    "a2l": ['ASAP2 database'],
    "a80": ['Assembly Z80 SjASM'],
    "ab": ['Automation Basic'],
    "abap": ['ABAP'],
    "abc": ['ABC Notation'],
    "acp": ['SynWrite acp files'],
    "ad": ['AsciiDoc'],
    "adb": ['Ada'],
    "ado": ['Stata'],
    "adoc": ['AsciiDoc'],
    "ads": ['Ada (.ads)'],
    "adxl": ['DOORS DXL'],
    "ahk": ['AutoHotkey'],
    "am": ['Automake'],
    "ampl": ['AMPL'],
    "applescript": ['AppleScript'],
    "arr": ['Pyret'],
    "as": ['ActionScript', 'Haskell'],
    "asciidoc": ['AsciiDoc'],
    "ash": ['Assembly FASM'],
    "astro": ['Astro'],
    "asy": ['Asymptote'],
    "au3": ['AutoIt'],
    "aux": ['LaTeX'],
    "avs": ['AviSynth'],
    "avsi": ['AviSynth'],
    "awk": ['AWK'],
    "b": ['Brainfuck'],
    "babel": ['JavaScript Babel'],
    "bal": ['Ballerina'],
    "bas": ['FreeBASIC', 'Great Cow Basic'],
    "bb": ['Clojure'],
    "bi": ['FreeBASIC'],
    "bib": ['BibTeX'],
    "bicep": ['Bicep'],
    "blade.php": ['HTML Laravel Blade'],
    "boo": ['Boo'],
    "boot": ['Clojure'],
    "btm": ['TakeCommand'],
    "capfile": ['Ruby'],
    "cbd": ['Cobol'],
    "cbl": ['Cobol', 'Acu Cobol'],
    "cc": ['Visual dBase'],
    "cdb": ['Cobol'],
    "cdc": ['Cobol'],
    "cdl": ['SPICE'],
    "cfm": ['ColdFusion'],
    "cfml": ['ColdFusion'],
    "cgi": ['Perl'],
    "cir": ['SPICE'],
    "cjsx": ['CoffeeScript'],
    "cl": ['OpenCL'],
    "cla": ['Clavier', 'Clarion'],
    "clj": ['Clojure'],
    "cljs": ['Clojure'],
    "cljc": ['Clojure'],
    "cljx": ['Clojure'],
    "clp": ['Clipper'],
    "cls": ['LaTeX', 'Rexx'],
    "clw": ['Clarion'],
    "cm": ['Standard ML'],
    "cmake": ['CMake'],
    "cmd": ['TakeCommand'],
    "cob": ['Cobol'],
    "coffee": ['CoffeeScript'],
    "coffee.erb": ['CoffeeScript'],
    "cr": ['Crystal'],
    "crf": ['CRF'],
    "cs": ['C#', 'GLSL'],
    "cshtml": ['Razor'],
    "cson": ['CoffeeScript'],
    "csx": ['C#'],
    "cu": ['CUDA C++'],
    "cuh": ['CUDA C++'],
    "d": ['D'],
    "dart": ['Dart'],
    "dfm": ['Delphi resources'],
    "dhall": ['Dhall'],
    "di": ['D'],
    "dif": ['Diff'],
    "diff": ['Diff'],
    "do": ['Stata'],
    "dot": ['Graphviz DOT'],
    "dpr": ['Pascal'],
    "dxl": ['DOORS DXL'],
    "dzn": ['MiniZinc'],
    "e": ['Eiffel', 'Specman'],
    "eia": ['G-code'],
    "ejs": ['HTML Embedded JS'],
    "elm": ['Elm'],
    "eps": ['PostScript'],
    "erl": ['Erlang'],
    "es6": ['JavaScript Babel'],
    "etlua": ['etlua Template'],
    "ex": ['Elixir', 'Euphoria'],
    "exs": ['Elixir'],
    "ext": ['Bohemia SQF'],
    "exw": ['Euphoria'],
    "f": ['Fortran', 'nnCron'],
    "f2k": ['Fortran'],
    "f90": ['Fortran'],
    "f95": ['Fortran'],
    "factor": ['Factor'],
    "fal": ['Falcon'],
    "fasm": ['Assembly FASM'],
    "feature": ['Gherkin'],
    "fish": ['Fish'],
    "fmx": ['Delphi resources'],
    "for": ['Fortran'],
    "fountain": ['Fountain'],
    "frag": ['GLSL'],
    "fs": ['GLSL', 'Forth', 'F#'],
    "fsh": ['GLSL'],
    "fshader": ['GLSL'],
    "fx": ['HLSL'],
    "fxh": ['HLSL'],
    "gcb": ['Great Cow Basic'],
    "gcode": ['G-code'],
    "gd": ['GDScript'],
    "gemini": ['Gemini'],
    "gemspec": ['Ruby'],
    "geom": ['GLSL'],
    "glsl": ['GLSL'],
    "gmi": ['Gemini'],
    "gms": ['GAMS'],
    "gnu": ['Gnuplot'],
    "gnuplot": ['Gnuplot'],
    "go": ['Go'],
    "gp": ['Gnuplot'],
    "gpi": ['Gnuplot'],
    "gpj": ['GHS Project'],
    "gql": ['GraphQL'],
    "gradle": ['Groovy'],
    "graphql": ['GraphQL'],
    "grm": ['Gold Parser'],
    "groovy": ['Groovy'],
    "gs": ['GLSL'],
    "gsh": ['GLSL'],
    "gshader": ['GLSL'],
    "gsp": ['Grails Server Pages'],
    "gv": ['Graphviz DOT'],
    "haml": ['Haml'],
    "handlebars": ['HTML Handlebars'],
    "handlebars.html": ['HTML Handlebars'],
    "hb": ['Harbour'],
    "hbr": ['HTML Handlebars'],
    "hbrs": ['HTML Handlebars'],
    "hbs": ['HTML Handlebars'],
    "hbx": ['Harbour'],
    "hex": ['Intel HEX'],
    "hjson": ['HJSON'],
    "hlsl": ['HLSL'],
    "hlsli": ['HLSL'],
    "hql": ['Apache Hive'],
    "hs": ['Haskell'],
    "hsp": ['SPICE'],
    "html.erb": ['HTML Ruby-ERB'],
    "hx": ['Haxe'],
    "i": ['Assembly Motorola 68k', 'OpenEdge ABL'],
    "idl": ['IDL files'],
    "idx": ['LaTeX'],
    "inc": ['Assembly FASM', 'Pawn', 'Assembly AVR', 'Pascal', 'Assembly NASM x86', 'Assembly Z80 SjASM', 'Assembly Z80 RGBDS'],
    "ino": ['Arduino'],
    "inp": ['Abaqus Keywords'],
    "ion": ['Amazon Ion'],
    "irbrc": ['Ruby'],
    "iss": ['Inno Setup'],
    "iuml": ['PlantUML'],
    "j": ['Jasmine JVM Assembler'],
    "j2": ['Jinja2'],
    "jade": ['Jade'],
    "jam": ['Perforce Jam'],
    "jav": ['Java'],
    "java": ['Java'],
    "jbuilder": ['Ruby'],
    "jcl": ['JCL'],
    "jl": ['Julia'],
    "jq": ['JQ'],
    "jsonnet": ['Jsonnet'],
    "jsx": ['JavaScript Babel'],
    "k": ['LS-DYNA'],
    "kix": ['KiXtart'],
    "kk": ['Koka'],
    "ksp": ['Kontakt Script Processor'],
    "kt": ['Kotlin'],
    "kts": ['Kotlin'],
    "kv": ['Kivy'],
    "kx": ['KiXtart'],
    "l": ['Yacc'],
    "las": ['Haskell'],
    "lcf": ['Delphi resources'],
    "ld": ['GHS Linker', 'GNU linker'],
    "ldxl": ['DOORS DXL'],
    "less": ['LESS'],
    "less.erb": ['LESS'],
    "lfm": ['Delphi resources'],
    "lhs": ['Haskell'],
    "libsonnet": ['Jsonnet'],
    "liquid": ['HTML Liquid'],
    "lisp": ['Lisp'],
    "livecodescript": ['LiveCode'],
    "lpr": ['Pascal'],
    "lsp": ['Lisp'],
    "lst": ['Grub4Dos'],
    "lxl": ['Delphi resources'],
    "m": ['Power Query M', 'Assembly SPARC', 'MATLAB', 'Objective-C'],
    "m2": ['Modula 2'],
    "m4": ['Autoconf M4'],
    "ma": ['Maya'],
    "mak": ['Makefile'],
    "mdl": ['SPICE'],
    "mediawiki": ['MediaWiki'],
    "mel": ['Maya'],
    "mel.erb": ['Maya'],
    "mf": ['Metafont'],
    "mib": ['MIB files (SNMP protocol)'],
    "ml": ['Standard ML', 'OCaml'],
    "mli": ['OCaml'],
    "mm": ['Objective-C'],
    "mnu": ['Visual dBase'],
    "mo": ['Modelica'],
    "mod": ['Oberon', 'Modula 2'],
    "monkey": ['Monkey'],
    "monkey2": ['Monkey'],
    "mos": ['Modelica'],
    "mpf": ['G-code'],
    "mustache": ['HTML Mustache'],
    "my": ['MIB files (SNMP protocol)'],
    "mzn": ['MiniZinc'],
    "n": ['Nemerle'],
    "nasm": ['Assembly NASM x86'],
    "nc": ['G-code'],
    "nim": ['Nim'],
    "nix": ['Nix'],
    "ngc": ['G-code'],
    "nsh": ['NSIS'],
    "nsi": ['NSIS'],
    "nsl": ['NSL Assembler'],
    "nut": ['Squirrel'],
    "ob2": ['Oberon'],
    "org": ['Org-mode'],
    "p": ['Pawn', 'Pascal', 'Parser3', 'OpenEdge ABL'],
    "pas": ['PAX_Pascal', 'Pascal'],
    "patch": ['Diff'],
    "pbs": ['Great Cow Basic'],
    "pch": ['Objective-C'],
    "pck": ['MySQL_Stored_Procedures', 'PL-SQL'],
    "pe": ['PECmd script'],
    "picl": ['PICL'],
    "pig": ['Apache Pig'],
    "pig.substituted": ['Apache Pig'],
    "pike": ['Pike'],
    "pkgbuild": ['PKGBUILD'],
    "pl": ['Prolog', 'Perl'],
    "plt": ['Prolog'],
    "plx": ['Perl'],
    "pm": ['Perl'],
    "pml": ['PyMOL'],
    "pmod": ['Pike'],
    "po": ['Properties'],
    "podspec": ['Ruby'],
    "pony": ['Pony'],
    "pp": ['Pascal', 'Puppet'],
    "ppc": ['Assembly PowerPC'],
    "pq": ['Power Query M'],
    "pqm": ['Power Query M'],
    "prawn": ['Ruby'],
    "prg": ['Visual dBase', 'Harbour', 'FoxPro', 'G-code'],
    "pro": ['IDL language'],
    "properties": ['Properties'],
    "proto": ['Protocol Buffers'],
    "prototxt": ['Caffe Prototxt'],
    "pryrc": ['Ruby'],
    "ps": ['PostScript'],
    "ps1": ['PowerShell'],
    "psc": ['Papyrus'],
    "pug": ['Pug'],
    "pwn": ['Pawn'],
    "pxd": ['Cython'],
    "pxi": ['Cython'],
    "pyx": ['Cython'],
    "q": ['Apache Hive'],
    "qbe": ['Visual dBase'],
    "ql": ['Apache Hive'],
    "qml": ['QML'],
    "qmlproject": ['QML'],
    "r": ['R'],
    "rabl": ['Ruby'],
    "rake": ['Ruby'],
    "raku": ['Raku'],
    "rakudoc": ['Raku'],
    "rakumod": ['Raku'],
    "rakutest": ['Raku'],
    "rb": ['Ruby'],
    "rbi": ['Ruby'],
    "rbx": ['Ruby'],
    "rc": ['GHS Script', 'Windows Resource Script', 'Rust'],
    "rc2": ['Windows Resource Script'],
    "re": ['ReasonML'],
    "red": ['Red'],
    "reds": ['Red'],
    "rei": ['ReasonML'],
    "rex": ['Rexx'],
    "rhtml": ['HTML Ruby-ERB'],
    "rjs": ['Ruby'],
    "rkt": ['Racket'],
    "rl": ['Ragel'],
    "ron": ['RON'],
    "rpg": ['RPG_IV'],
    "rpgle": ['RPG_IV'],
    "rs": ['Rust'],
    "rsc": ['MikroTik Script'],
    "rtf": ['RTF'],
    "s": ['Assembly ARM', 'Assembly GNU AS', 'Assembly Motorola 68k', 'Assembly MIPS', 'Assembly RISC-V', 'Assembly SPARC', 'Assembly Z80 RGBDS'],
    "sass": ['Sass'],
    "sbt": ['Scala'],
    "scad": ['OpenSCAD'],
    "scala": ['Scala'],
    "sce": ['Scilab'],
    "sci": ['Scilab'],
    "scm": ['Scheme'],
    "scp": ['MacroScript (Macro Sheduler)'],
    "script": ['WinBuilder script'],
    "scss": ['SCSS'],
    "scss.erb": ['SCSS'],
    "sfz": ['SFZ'],
    "sig": ['Standard ML'],
    "simplecov": ['Ruby'],
    "sjson": ['Bitsquid SJSON'],
    "slim": ['Slim'],
    "sln": ['MSVS Solution'],
    "smali": ['Dalvik bytecode'],
    "smd": ['Scheme'],
    "sml": ['Standard ML'],
    "snowql": ['Snowflake SQL'],
    "sol": ['Solidity'],
    "sp": ['SPICE'],
    "spf": ['nnCron'],
    "spir-v": ['SPIR'],
    "spirv": ['SPIR'],
    "spv": ['SPIR'],
    "spvasm": ['SPIR'],
    "srt": ['SRT Subtitles'],
    "sqf": ['Bohemia SQF'],
    "sqm": ['Bohemia SQF'],
    "sqs": ['Bohemia SQF'],
    "ss": ['Scheme'],
    "st": ['Smalltalk'],
    "str": ['TypeScript'],
    "strace": ['Strace'],
    "sty": ['LaTeX'],
    "styl": ['Stylus'],
    "svelte": ['Svelte'],
    "svlt": ['Svelte'],
    "swift": ['Swift'],
    "synw-snippet": ['SynWrite snippets'],
    "tab": ['nnCron'],
    "tagml": ['TAGML'],
    "taskpaper": ['ToDo'],
    "tasks": ['ToDo'],
    "tcl": ['Tcl'],
    "tdxl": ['DOORS DXL'],
    "template": ['HTML Handlebars'],
    "tes": ['GLSL'],
    "tex": ['LaTeX'],
    "textile": ['Textile'],
    "thor": ['Ruby'],
    "tk": ['Tcl'],
    "tm": ['Tcl'],
    "tmpl": ['HTML Handlebars'],
    "toc": ['LaTeX'],
    "todo": ['ToDo'],
    "todolist": ['ToDo'],
    "toml": ['TOML'],
    "tpl": ['HTML Smarty'],
    "tql": ['T-SQL'],
    "tree": ['Tree'],
    "ts": ['TypeScript'],
    "tsc": ['GLSL'],
    "tsx": ['TypeScript'],
    "twig": ['Twig'],
    "tx": ['Textile'],
    "uml": ['PlantUML'],
    "usf": ['HLSL'],
    "v": ['Coq', 'V', 'Verilog HDL'],
    "v3": ['Virgil'],
    "vala": ['Vala'],
    "vapi": ['Vala'],
    "var": ['Automation Basic'],
    "vbhtml": ['Razor'],
    "vert": ['GLSL'],
    "vhdl": ['VHDL'],
    "vim": ['VimL'],
    "vm": ['Java Velocity'],
    "vs": ['GLSL'],
    "vsh": ['GLSL'],
    "vshader": ['GLSL'],
    "vue": ['Vue'],
    "w": ['OpenEdge ABL'],
    "wcs": ['PECmd script'],
    "wfm": ['Visual dBase'],
    "wiki": ['WikidPad', 'MediaWiki'],
    "wikipedia": ['MediaWiki'],
    "wsc": ['PECmd script'],
    "wsd": ['PlantUML'],
    "wsf": ['WSH script'],
    "xfm": ['Delphi resources'],
    "xsl": ['XSLT'],
    "xslt": ['XSLT'],
    "y": ['Yacc'],
    "zep": ['Zephir'],
    "zig": ['Zig'],
    "zs": ['ZenScript (MineTweaker)'],
}
