

    
class Default():
    '''Provide the preferences to the application'''
    def __init__(self):
        pass


    def theme_xml_string(self):
        s = '''<?xml version="1.0" encoding="UTF-8" ?>
<styles>
    <LexerStyles>
        <LexerType name="actionscript" desc="ActionScript" ext="">
            <WordsStyle name="DEFAULT" styleID="11" fgColor="000000" bgColor="FFFFFF" fontName="" fontStyle="0" fontSize="" />
            <WordsStyle name="FUNCTION" styleID="20" fgColor="95004A" bgColor="FFFFFF" fontName="" fontStyle="0" fontSize="" keywordClass="type2" />
            <WordsStyle name="PREPROCESSOR" styleID="9" fgColor="804000" bgColor="FFFFFF" fontName="" fontStyle="0" fontSize="" />
            <WordsStyle name="INSTRUCTION WORD" styleID="5" fgColor="0000FF" bgColor="FFFFFF" fontName="" fontStyle="1" fontSize="" keywordClass="instre1" />
            <WordsStyle name="TYPE WORD" styleID="16" fgColor="8000FF" bgColor="FFFFFF" fontName="" fontStyle="0" fontSize="" keywordClass="type1" />
            <WordsStyle name="NUMBER" styleID="4" fgColor="FF8000" bgColor="FFFFFF" fontName="" fontStyle="0" fontSize="" />
            <WordsStyle name="STRING" styleID="6" fgColor="808080" bgColor="FFFFFF" fontName="" fontStyle="0" fontSize="" />
            <WordsStyle name="CHARACTER" styleID="7" fgColor="808080" bgColor="FFFFFF" fontName="" fontStyle="0" fontSize="" />
            <WordsStyle name="OPERATOR" styleID="10" fgColor="000080" bgColor="FFFFFF" fontName="" fontStyle="1" fontSize="" />
            <WordsStyle name="VERBATIM" styleID="13" fgColor="808080" bgColor="FFFFFF" fontName="" fontStyle="1" fontSize="" />
            <WordsStyle name="REGEX" styleID="14" fgColor="000000" bgColor="FFFFFF" fontName="" fontStyle="1" fontSize="" />
            <WordsStyle name="COMMENT" styleID="1" fgColor="008000" bgColor="FFFFFF" fontName="" fontStyle="0" fontSize="" />
            <WordsStyle name="COMMENT LINE" styleID="2" fgColor="008000" bgColor="FFFFFF" fontName="" fontStyle="0" fontSize="" />
            <WordsStyle name="COMMENT DOC" styleID="3" fgColor="008080" bgColor="FFFFFF" fontName="" fontStyle="0" fontSize="" />
            <WordsStyle name="COMMENT LINE DOC" styleID="15" fgColor="008080" bgColor="FFFFFF" fontName="" fontStyle="0" fontSize="" />
            <WordsStyle name="COMMENT DOC KEYWORD" styleID="17" fgColor="008080" bgColor="FFFFFF" fontName="" fontStyle="1" fontSize="" />
            <WordsStyle name="COMMENT DOC KEYWORD ERROR" styleID="18" fgColor="008080" bgColor="FFFFFF" fontName="" fontStyle="0" fontSize="" />
        </LexerType>
        <LexerType name="ada" desc="ADA" ext="">
            <WordsStyle name="DEFAULT" styleID="0" fgColor="000000" bgColor="FFFFFF" fontName="" fontStyle="0" fontSize="" />
            <WordsStyle name="INSTRUCTION WORD" styleID="1" fgColor="0000FF" bgColor="FFFFFF" fontName="" fontStyle="1" fontSize="" keywordClass="instre1" />
            <WordsStyle name="IDENTIFIER" styleID="2" fgColor="000000" bgColor="FFFFFF" fontName="" fontStyle="0" fontSize="" />
            <WordsStyle name="NUMBER" styleID="3" fgColor="FF8000" bgColor="FFFFFF" fontName="" fontStyle="0" fontSize="" />
            <WordsStyle name="DELIMITER" styleID="4" fgColor="FF8080" bgColor="FFFFFF" fontName="" fontStyle="1" fontSize="" />
            <WordsStyle name="CHARACTER" styleID="5" fgColor="808080" bgColor="FFFFFF" fontName="" fontStyle="0" fontSize="" />
            <WordsStyle name="STRING" styleID="7" fgColor="808080" bgColor="FFFFFF" fontName="" fontStyle="0" fontSize="" />
            <WordsStyle name="LABEL" styleID="9" fgColor="804000" bgColor="FFFFFF" fontName="" fontStyle="1" fontSize="" />
            <WordsStyle name="COMMENT LINE" styleID="10" fgColor="008000" bgColor="FFFFFF" fontName="" fontStyle="0" fontSize="" />
            <WordsStyle name="ILLEGAL" styleID="11" fgColor="FF0000" bgColor="FFFFFF" fontName="" fontStyle="0" fontSize="" />
        </LexerType>
        <LexerType name="asp" desc="asp" ext="asp">
            <WordsStyle name="DEFAULT" styleID="81" fgColor="8000FF" bgColor="C4F9FD" fontName="" fontStyle="0" fontSize="" />
            <WordsStyle name="COMMENTLINE" styleID="82" fgColor="008000" bgColor="C4F9FD" fontName="" fontStyle="0" fontSize="" />
            <WordsStyle name="NUMBER" styleID="83" fgColor="FF0000" bgColor="C4F9FD" fontName="" fontStyle="0" fontSize="" />
            <WordsStyle name="WORD" styleID="84" fgColor="000080" bgColor="C4F9FD" fontName="" fontStyle="1" fontSize="" keywordClass="instre1" />
            <WordsStyle name="STRING" styleID="85" fgColor="808080" bgColor="C4F9FD" fontName="" fontStyle="0" fontSize="" />
            <WordsStyle name="IDENTIFIER" styleID="86" fgColor="000000" bgColor="C4F9FD" fontName="" fontStyle="0" fontSize="" />
            <WordsStyle name="ASPSYBOL" styleID="15" fgColor="000000" bgColor="FFFF00" fontName="" fontStyle="1" fontSize="" />
            <WordsStyle name="SCRIPTTYPE" styleID="16" fgColor="000000" bgColor="FFC000" fontName="" fontStyle="0" fontSize="" />
        </LexerType>
        <LexerType name="asm" desc="Assembly" ext="">
            <WordsStyle name="DEFAULT" styleID="0" fgColor="000000" bgColor="FFFFFF" fontName="" fontStyle="0" fontSize="" />
            <WordsStyle name="COMMENT" styleID="1" fgColor="008000" bgColor="FFFFFF" fontName="" fontStyle="0" fontSize="" />
            <WordsStyle name="NUMBER" styleID="2" fgColor="FF8000" bgColor="FFFFFF" fontName="" fontStyle="0" fontSize="" />
            <WordsStyle name="STRING" styleID="3" fgColor="808080" bgColor="FFFFFF" fontName="" fontStyle="0" fontSize="" />
            <WordsStyle name="OPERATOR" styleID="4" fgColor="000080" bgColor="FFFFFF" fontName="" fontStyle="1" fontSize="" />
            <WordsStyle name="IDENTIFIER" styleID="5" fgColor="000000" bgColor="FFFFFF" fontName="" fontStyle="0" fontSize="" />
            <WordsStyle name="CPU INSTRUCTION" styleID="6" fgColor="0000FF" bgColor="FFFFFF" fontName="" fontStyle="1" fontSize="" keywordClass="instre1" />
            <WordsStyle name="MATH INSTRUCTION" styleID="7" fgColor="0080C0" bgColor="FFFFFF" fontName="" fontStyle="1" fontSize="" keywordClass="instre2" />
            <WordsStyle name="REGISTER" styleID="8" fgColor="8080FF" bgColor="FFFFCC" fontName="" fontStyle="1" fontSize="" keywordClass="type1" />
            <WordsStyle name="DIRECTIVE" styleID="9" fgColor="0080FF" bgColor="FFFFFF" fontName="" fontStyle="0" fontSize="" keywordClass="type2" />
            <WordsStyle name="DIRECTIVE OPERAND" styleID="10" fgColor="000080" bgColor="FFFFFF" fontName="" fontStyle="1" fontSize="" keywordClass="type3" />
            <WordsStyle name="COMMENT BLOCK" styleID="11" fgColor="008000" bgColor="FFFFFF" fontName="" fontStyle="0" fontSize="" />
            <WordsStyle name="CHARACTER" styleID="12" fgColor="808000" bgColor="FFFFFF" fontName="" fontStyle="0" fontSize="" />
            <WordsStyle name="EXT INSTRUCTION" styleID="14" fgColor="804000" bgColor="FFFFFF" fontName="" fontStyle="1" fontSize="" keywordClass="type4" />
        </LexerType>
        <LexerType name="autoit" desc="autoIt" ext="">
            <WordsStyle name="DEFAULT" styleID="0" fgColor="000000" bgColor="FFFFFF" fontName="" fontStyle="0" fontSize="" />
            <WordsStyle name="COMMENT LINE" styleID="1" fgColor="008000" bgColor="FFFFFF" fontName="" fontStyle="0" fontSize="" />
            <WordsStyle name="COMMENT" styleID="2" fgColor="008000" bgColor="FFFFFF" fontName="" fontStyle="0" fontSize="" />
            <WordsStyle name="NUMBER" styleID="3" fgColor="FF8000" bgColor="FFFFFF" fontName="" fontStyle="0" fontSize="" />
            <WordsStyle name="FUNCTION" styleID="4" fgColor="8000FF" bgColor="FFFFFF" fontName="" fontStyle="0" fontSize="" keywordClass="instre2" />
            <WordsStyle name="INSTRUCTION WORD" styleID="5" fgColor="0000FF" bgColor="FFFFFF" fontName="" fontStyle="1" fontSize="" keywordClass="instre1" />
            <WordsStyle name="MACRO" styleID="6" fgColor="8000FF" bgColor="FFFFFF" fontName="" fontStyle="0" fontSize="" keywordClass="type1" />
            <WordsStyle name="STRING" styleID="7" fgColor="808080" bgColor="FFFFFF" fontName="" fontStyle="0" fontSize="" />
            <WordsStyle name="OPERATOR" styleID="8" fgColor="000080" bgColor="FFFFFF" fontName="" fontStyle="1" fontSize="" />
            <WordsStyle name="VARIABLE" styleID="9" fgColor="FF0080" bgColor="FFFFFF" fontName="" fontStyle="2" fontSize="" />
            <WordsStyle name="SENT" styleID="10" fgColor="8080C0" bgColor="FFFFFF" fontName="" fontStyle="0" fontSize="" keywordClass="type2" />
            <WordsStyle name="PREPROCESSOR" styleID="11" fgColor="804000" bgColor="FFFFFF" fontName="" fontStyle="0" fontSize="" keywordClass="type3" />
            <WordsStyle name="SPECIAL" styleID="12" fgColor="000000" bgColor="FFFFFF" fontName="" fontStyle="0" fontSize="" keywordClass="type4" />
            <WordsStyle name="EXPAND" styleID="13" fgColor="000000" bgColor="FFFFFF" fontName="" fontStyle="0" fontSize="" keywordClass="type5" />
            <WordsStyle name="COMOBJ" styleID="14" fgColor="000000" bgColor="FFFFFF" fontName="" fontStyle="0" fontSize="" />
        </LexerType>
        <LexerType name="Bash" desc="Bash" ext="">
            <WordsStyle name="DEFAULT" styleID="0" fgColor="000000" bgColor="FFFFFF" fontName="" fontStyle="0" fontSize="" />
            <WordsStyle name="ERROR" styleID="1" fgColor="FFFFFF" bgColor="FF0000" fontName="" fontStyle="0" fontSize="" />
            <WordsStyle name="INSTRUCTION WORD" styleID="4" fgColor="0000FF" bgColor="FFFFFF" fontName="" fontStyle="1" fontSize="" keywordClass="instre1" />
            <WordsStyle name="NUMBER" styleID="3" fgColor="FF0000" bgColor="FFFFFF" fontName="" fontStyle="0" fontSize="" />
            <WordsStyle name="STRING" styleID="5" fgColor="808080" bgColor="FFFFFF" fontName="" fontStyle="0" fontSize="" />
            <WordsStyle name="CHARACTER" styleID="6" fgColor="808080" bgColor="FFFFFF" fontName="" fontStyle="0" fontSize="" />
            <WordsStyle name="OPERATOR" styleID="7" fgColor="804000" bgColor="FFFFFF" fontName="" fontStyle="1" fontSize="" />
            <WordsStyle name="IDENTIFIER" styleID="8" fgColor="000000" bgColor="FFFFFF" fontName="" fontStyle="0" fontSize="" />
            <WordsStyle name="SCALAR" styleID="9" fgColor="FF8040" bgColor="FFFFD9" fontName="" fontStyle="1" fontSize="" />
            <WordsStyle name="COMMENT LINE" styleID="2" fgColor="008000" bgColor="FFFFFF" fontName="" fontStyle="0" fontSize="" />
            <WordsStyle name="PARAM" styleID="10" fgColor="008080" bgColor="00FFFF" fontName="" fontStyle="0" fontSize="" />
            <WordsStyle name="BACKTICKS" styleID="11" fgColor="804040" bgColor="E1FFF3" fontName="" fontStyle="1" fontSize="" />
            <WordsStyle name="HERE DELIM" styleID="12" fgColor="0000FF" bgColor="FF0000" fontName="" fontStyle="1" fontSize="" />
            <WordsStyle name="HERE Q" styleID="13" fgColor="FF0000" bgColor="0000FF" fontName="" fontStyle="0" fontSize="" />
        </LexerType>
        <LexerType name="batch" desc="Batch" ext="">
            <WordsStyle name="DEFAULT" styleID="0" fgColor="000000" bgColor="FFFFFF" fontName="" fontStyle="0" fontSize="" />
            <WordsStyle name="COMMENT" styleID="1" fgColor="008000" bgColor="FFFFFF" fontName="" fontStyle="0" fontSize="" />
            <WordsStyle name="KEYWORDS" styleID="2" fgColor="0000FF" bgColor="FFFFFF" fontName="" fontStyle="1" fontSize="" keywordClass="instre1" />
            <WordsStyle name="LABEL" styleID="3" fgColor="FF0000" bgColor="FFFF80" fontName="" fontStyle="1" fontSize="" />
            <WordsStyle name="HIDE SYBOL" styleID="4" fgColor="FF00FF" bgColor="FFFFFF" fontName="" fontStyle="0" fontSize="" />
            <WordsStyle name="COMMAND" styleID="5" fgColor="0080FF" bgColor="FFFFFF" fontName="" fontStyle="0" fontSize="" />
            <WordsStyle name="VARIABLE" styleID="6" fgColor="FF8000" bgColor="FCFFF0" fontName="" fontStyle="1" fontSize="" />
            <WordsStyle name="OPERATOR" styleID="7" fgColor="FF0000" bgColor="FFFFFF" fontName="" fontStyle="1" fontSize="" />
        </LexerType>
        <LexerType name="c" desc="C" ext="">
            <WordsStyle name="PREPROCESSOR" styleID="9" fgColor="804000" bgColor="FFFFFF" fontName="" fontStyle="0" fontSize="" />
            <WordsStyle name="DEFAULT" styleID="11" fgColor="000000" bgColor="FFFFFF" fontName="" fontStyle="0" fontSize="" />
            <WordsStyle name="INSTRUCTION WORD" styleID="5" fgColor="0000FF" bgColor="FFFFFF" fontName="" fontStyle="1" fontSize="" keywordClass="instre1" />
            <WordsStyle name="TYPE WORD" styleID="16" fgColor="8000FF" bgColor="FFFFFF" fontName="" fontStyle="0" fontSize="" keywordClass="type1" />
            <WordsStyle name="NUMBER" styleID="4" fgColor="FF8000" bgColor="FFFFFF" fontName="" fontStyle="0" fontSize="" />
            <WordsStyle name="STRING" styleID="6" fgColor="808080" bgColor="FFFFFF" fontName="" fontStyle="0" fontSize="" />
            <WordsStyle name="CHARACTER" styleID="7" fgColor="808080" bgColor="FFFFFF" fontName="" fontStyle="0" fontSize="" />
            <WordsStyle name="OPERATOR" styleID="10" fgColor="000080" bgColor="FFFFFF" fontName="" fontStyle="1" fontSize="" />
            <WordsStyle name="VERBATIM" styleID="13" fgColor="000000" bgColor="FFFFFF" fontName="" fontStyle="0" fontSize="" />
            <WordsStyle name="REGEX" styleID="14" fgColor="000000" bgColor="FFFFFF" fontName="" fontStyle="1" fontSize="" />
            <WordsStyle name="COMMENT" styleID="1" fgColor="008000" bgColor="FFFFFF" fontName="" fontStyle="0" fontSize="" />
            <WordsStyle name="COMMENT LINE" styleID="2" fgColor="008000" bgColor="FFFFFF" fontName="" fontStyle="0" fontSize="" />
            <WordsStyle name="COMMENT DOC" styleID="3" fgColor="008080" bgColor="FFFFFF" fontName="" fontStyle="0" fontSize="" />
            <WordsStyle name="COMMENT LINE DOC" styleID="15" fgColor="008080" bgColor="FFFFFF" fontName="" fontStyle="0" fontSize="" />
            <WordsStyle name="COMMENT DOC KEYWORD" styleID="17" fgColor="008080" bgColor="FFFFFF" fontName="" fontStyle="1" fontSize="" />
            <WordsStyle name="COMMENT DOC KEYWORD ERROR" styleID="18" fgColor="008080" bgColor="FFFFFF" fontName="" fontStyle="0" fontSize="" />
        </LexerType>
        <LexerType name="cpp" desc="C++" ext="">
            <WordsStyle name="PREPROCESSOR" styleID="9" fgColor="804000" bgColor="FFFFFF" fontName="" fontStyle="0" fontSize="" />
            <WordsStyle name="DEFAULT" styleID="11" fgColor="000000" bgColor="FFFFFF" fontName="" fontStyle="0" fontSize="" />
            <WordsStyle name="INSTRUCTION WORD" styleID="5" fgColor="0000FF" bgColor="FFFFFF" fontName="" fontStyle="1" fontSize="" keywordClass="instre1" />
            <WordsStyle name="TYPE WORD" styleID="16" fgColor="8000FF" bgColor="FFFFFF" fontName="" fontStyle="0" fontSize="" keywordClass="type1" />
            <WordsStyle name="NUMBER" styleID="4" fgColor="FF8000" bgColor="FFFFFF" fontName="" fontStyle="0" fontSize="" />
            <WordsStyle name="STRING" styleID="6" fgColor="808080" bgColor="FFFFFF" fontName="" fontStyle="0" fontSize="" />
            <WordsStyle name="CHARACTER" styleID="7" fgColor="808080" bgColor="FFFFFF" fontName="" fontStyle="0" fontSize="" />
            <WordsStyle name="OPERATOR" styleID="10" fgColor="000080" bgColor="FFFFFF" fontName="" fontStyle="1" fontSize="" />
            <WordsStyle name="VERBATIM" styleID="13" fgColor="000000" bgColor="FFFFFF" fontName="" fontStyle="0" fontSize="" />
            <WordsStyle name="REGEX" styleID="14" fgColor="000000" bgColor="FFFFFF" fontName="" fontStyle="1" fontSize="" />
            <WordsStyle name="COMMENT" styleID="1" fgColor="008000" bgColor="FFFFFF" fontName="" fontStyle="0" fontSize="" />
            <WordsStyle name="COMMENT LINE" styleID="2" fgColor="008000" bgColor="FFFFFF" fontName="" fontStyle="0" fontSize="" />
            <WordsStyle name="COMMENT DOC" styleID="3" fgColor="008080" bgColor="FFFFFF" fontName="" fontStyle="0" fontSize="" />
            <WordsStyle name="COMMENT LINE DOC" styleID="15" fgColor="008080" bgColor="FFFFFF" fontName="" fontStyle="0" fontSize="" />
            <WordsStyle name="COMMENT DOC KEYWORD" styleID="17" fgColor="008080" bgColor="FFFFFF" fontName="" fontStyle="1" fontSize="" />
            <WordsStyle name="COMMENT DOC KEYWORD ERROR" styleID="18" fgColor="008080" bgColor="FFFFFF" fontName="" fontStyle="0" fontSize="" />
        </LexerType>
        <LexerType name="cs" desc="C#" ext="">
            <WordsStyle name="PREPROCESSOR" styleID="9" fgColor="804000" bgColor="FFFFFF" fontName="" fontStyle="0" fontSize="" />
            <WordsStyle name="DEFAULT" styleID="11" fgColor="000000" bgColor="FFFFFF" fontName="" fontStyle="0" fontSize="" />
            <WordsStyle name="INSTRUCTION WORD" styleID="5" fgColor="0000FF" bgColor="FFFFFF" fontName="" fontStyle="1" fontSize="" keywordClass="instre1" />
            <WordsStyle name="TYPE WORD" styleID="16" fgColor="8000FF" bgColor="FFFFFF" fontName="" fontStyle="0" fontSize="" />
            <WordsStyle name="NUMBER" styleID="4" fgColor="FF8000" bgColor="FFFFFF" fontName="" fontStyle="0" fontSize="" />
            <WordsStyle name="STRING" styleID="6" fgColor="808080" bgColor="FFFFFF" fontName="" fontStyle="0" fontSize="" />
            <WordsStyle name="CHARACTER" styleID="7" fgColor="808080" bgColor="FFFFFF" fontName="" fontStyle="0" fontSize="" />
            <WordsStyle name="OPERATOR" styleID="10" fgColor="000080" bgColor="FFFFFF" fontName="" fontStyle="1" fontSize="" />
            <WordsStyle name="VERBATIM" styleID="13" fgColor="000000" bgColor="FFFFFF" fontName="" fontStyle="0" fontSize="" />
            <WordsStyle name="REGEX" styleID="14" fgColor="000000" bgColor="FFFFFF" fontName="" fontStyle="1" fontSize="" />
            <WordsStyle name="COMMENT" styleID="1" fgColor="008000" bgColor="FFFFFF" fontName="" fontStyle="0" fontSize="" />
            <WordsStyle name="COMMENT LINE" styleID="2" fgColor="008000" bgColor="FFFFFF" fontName="" fontStyle="0" fontSize="" />
            <WordsStyle name="COMMENT DOC" styleID="3" fgColor="008080" bgColor="FFFFFF" fontName="" fontStyle="0" fontSize="" />
            <WordsStyle name="COMMENT LINE DOC" styleID="15" fgColor="008080" bgColor="FFFFFF" fontName="" fontStyle="0" fontSize="" />
            <WordsStyle name="COMMENT DOC KEYWORD" styleID="17" fgColor="008080" bgColor="FFFFFF" fontName="" fontStyle="1" fontSize="" />
            <WordsStyle name="COMMENT DOC KEYWORD ERROR" styleID="18" fgColor="008080" bgColor="FFFFFF" fontName="" fontStyle="0" fontSize="" />
        </LexerType>
        <LexerType name="caml" desc="Caml" ext="">
            <WordsStyle name="DEFAULT" styleID="0" fgColor="000000" bgColor="FFFFFF" fontName="" fontStyle="0" fontSize="" />
            <WordsStyle name="IDENTIFIER" styleID="1" fgColor="000000" bgColor="FFFFFF" fontName="" fontStyle="0" fontSize="" />
            <WordsStyle name="TAGNAME" styleID="2" fgColor="000000" bgColor="FFFFFF" fontName="" fontStyle="0" fontSize="" />
            <WordsStyle name="INSTRUCTION WORD" styleID="3" fgColor="0000FF" bgColor="FFFFFF" fontName="" fontStyle="1" fontSize="" keywordClass="instre1" />
            <WordsStyle name="BUILIN FUNC &amp; TYPE" styleID="4" fgColor="8000FF" bgColor="FFFFFF" fontName="" fontStyle="0" fontSize="" keywordClass="instre2" />
            <WordsStyle name="TYPE" styleID="5" fgColor="8000FF" bgColor="FFFFFF" fontName="" fontStyle="0" fontSize="" keywordClass="type1" />
            <WordsStyle name="LINENUM" styleID="6" fgColor="000000" bgColor="FFFFFF" fontName="" fontStyle="1" fontSize="" />
            <WordsStyle name="OPERATOR" styleID="7" fgColor="000080" bgColor="FFFFFF" fontName="" fontStyle="1" fontSize="" />
            <WordsStyle name="NUMBER" styleID="8" fgColor="FF8000" bgColor="FFFFFF" fontName="" fontStyle="0" fontSize="" />
            <WordsStyle name="CHARACTER" styleID="9" fgColor="808080" bgColor="FFFFFF" fontName="" fontStyle="0" fontSize="" />
            <WordsStyle name="STRING" styleID="11" fgColor="808080" bgColor="FFFFFF" fontName="" fontStyle="0" fontSize="" />
            <WordsStyle name="COMMENT" styleID="12" fgColor="008000" bgColor="FFFFFF" fontName="" fontStyle="0" fontSize="" />
            <WordsStyle name="COMMENT LINE" styleID="13" fgColor="008000" bgColor="FFFFFF" fontName="" fontStyle="0" fontSize="" />
            <WordsStyle name="COMMENT DOC" styleID="14" fgColor="008080" bgColor="FFFFFF" fontName="" fontStyle="0" fontSize="" />
            <WordsStyle name="COMMENT LINE DOC" styleID="15" fgColor="008080" bgColor="FFFFFF" fontName="" fontStyle="0" fontSize="" />
        </LexerType>
        <LexerType name="cmake" desc="CMakeFile" ext="cmake">
            <WordsStyle name="DEFAULT" styleID="0" fgColor="000000" bgColor="FFFFFF" fontName="" fontStyle="0" fontSize="" />
            <WordsStyle name="COMMENT" styleID="1" fgColor="008000" bgColor="FFFFFF" fontName="" fontStyle="0" fontSize="" />
            <WordsStyle name="STRING D" styleID="2" fgColor="808080" bgColor="FFFFFF" fontName="" fontStyle="0" fontSize="" />
            <WordsStyle name="STRING L" styleID="3" fgColor="808080" bgColor="FFFFFF" fontName="" fontStyle="2" fontSize="" />
            <WordsStyle name="STRING R" styleID="4" fgColor="808080" bgColor="FFFFFF" fontName="" fontStyle="4" fontSize="" />
            <WordsStyle name="COMMAND" styleID="5" fgColor="0000FF" bgColor="FFFFFF" fontName="" fontStyle="1" fontSize="" keywordClass="instre1" />
            <WordsStyle name="PARAMETER" styleID="6" fgColor="8000FF" bgColor="FFFFFF" fontName="" fontStyle="0" fontSize="" />
            <WordsStyle name="VARIABLE" styleID="7" fgColor="FF8040" bgColor="FFFFFF" fontName="" fontStyle="0" fontSize="" />
            <WordsStyle name="USER DEFINED" styleID="8" fgColor="000080" bgColor="FFFFFF" fontName="" fontStyle="1" fontSize="" keywordClass="type1" />
            <WordsStyle name="WHILEDEF" styleID="9" fgColor="0080FF" bgColor="FFFFFF" fontName="" fontStyle="1" fontSize="" />
            <WordsStyle name="FOREACHDEF" styleID="10" fgColor="008080" bgColor="FFFFFF" fontName="" fontStyle="1" fontSize="" />
            <WordsStyle name="IFDEF" styleID="11" fgColor="8000FF" bgColor="FFFFFF" fontName="" fontStyle="1" fontSize="" />
            <WordsStyle name="MACRODEF" styleID="12" fgColor="FF0000" bgColor="FFFFFF" fontName="" fontStyle="1" fontSize="" />
            <WordsStyle name="STRING VARIABLE" styleID="13" fgColor="808080" bgColor="FEFCF5" fontName="" fontStyle="1" fontSize="" />
            <WordsStyle name="NUMBER" styleID="14" fgColor="804040" bgColor="FFFFFF" fontName="" fontStyle="1" fontSize="" />
        </LexerType>
        <LexerType name="css" desc="CSS" ext="">
            <WordsStyle name="DEFAULT" styleID="0" fgColor="000000" bgColor="FFFFFF" fontName="" fontStyle="0" fontSize="" />
            <WordsStyle name="TAG" styleID="1" fgColor="0000FF" bgColor="FFFFFF" fontName="Batang" fontStyle="0" fontSize="" />
            <WordsStyle name="CLASS" styleID="2" fgColor="FF0000" bgColor="FFFFFF" fontName="" fontStyle="0" fontSize="" />
            <WordsStyle name="PSEUDOCLASS" styleID="3" fgColor="FF8000" bgColor="FFFFFF" fontName="" fontStyle="1" fontSize="" />
            <WordsStyle name="UNKNOWN_PSEUDOCLASS" styleID="4" fgColor="FF8080" bgColor="FFFFFF" fontName="" fontStyle="0" fontSize="" />
            <WordsStyle name="OPERATOR" styleID="5" fgColor="000000" bgColor="FFFFFF" fontName="" fontStyle="1" fontSize="" />
            <WordsStyle name="IDENTIFIER" styleID="6" fgColor="8080C0" bgColor="FFFFFF" fontName="" fontStyle="1" fontSize="" keywordClass="instre1" />
            <WordsStyle name="UNKNOWN_IDENTIFIER" styleID="7" fgColor="000000" bgColor="FFFFFF" fontName="" fontStyle="0" fontSize="" />
            <WordsStyle name="VALUE" styleID="8" fgColor="000000" bgColor="FFFFFF" fontName="" fontStyle="1" fontSize="" />
            <WordsStyle name="COMMENT" styleID="9" fgColor="008000" bgColor="FFFFFF" fontName="" fontStyle="0" fontSize="" />
            <WordsStyle name="ID" styleID="10" fgColor="0080FF" bgColor="FFFFFF" fontName="" fontStyle="1" fontSize="" />
            <WordsStyle name="IMPORTANT" styleID="11" fgColor="FF0000" bgColor="FFFFFF" fontName="" fontStyle="1" fontSize="" />
            <WordsStyle name="DIRECTIVE" styleID="12" fgColor="0080FF" bgColor="FFFFFF" fontName="" fontStyle="0" fontSize="" />
        </LexerType>
        <LexerType name="cobol" desc="COBOL" ext="">
            <WordsStyle name="PREPROCESSOR" styleID="9" fgColor="804000" bgColor="FFFFFF" fontName="" fontStyle="0" fontSize="" />
            <WordsStyle name="DEFAULT" styleID="11" fgColor="000000" bgColor="FFFFFF" fontName="" fontStyle="0" fontSize="" />
            <WordsStyle name="DECLARATION" styleID="5" fgColor="8000FF" bgColor="FFFFFF" fontName="" fontStyle="1" fontSize="" keywordClass="instre1" />
            <WordsStyle name="INSTRUCTION WORD" styleID="16" fgColor="0000FF" bgColor="FFFFFF" fontName="" fontStyle="1" fontSize="" keywordClass="instre2" />
            <WordsStyle name="KEYWORD" styleID="8" fgColor="0080FF" bgColor="FFFFFF" fontName="" fontStyle="0" fontSize="" keywordClass="type1" />
            <WordsStyle name="NUMBER" styleID="4" fgColor="FF8000" bgColor="FFFFFF" fontName="" fontStyle="0" fontSize="" />
            <WordsStyle name="STRING" styleID="6" fgColor="808080" bgColor="FFFFFF" fontName="" fontStyle="0" fontSize="" />
            <WordsStyle name="CHARACTER" styleID="7" fgColor="808080" bgColor="FFFFFF" fontName="" fontStyle="0" fontSize="" />
            <WordsStyle name="OPERATOR" styleID="10" fgColor="000080" bgColor="FFFFFF" fontName="" fontStyle="1" fontSize="" />
            <WordsStyle name="COMMENT" styleID="1" fgColor="008000" bgColor="FFFFFF" fontName="" fontStyle="0" fontSize="" />
            <WordsStyle name="COMMENT LINE" styleID="2" fgColor="008000" bgColor="FFFFFF" fontName="" fontStyle="0" fontSize="" />
            <WordsStyle name="COMMENT DOC" styleID="3" fgColor="008080" bgColor="FFFFFF" fontName="" fontStyle="0" fontSize="" />
            <WordsStyle name="COMMENT LINE DOC" styleID="15" fgColor="008080" bgColor="FFFFFF" fontName="" fontStyle="0" fontSize="" />
            <WordsStyle name="COMMENT DOC KEYWORD" styleID="17" fgColor="008080" bgColor="FFFFFF" fontName="" fontStyle="1" fontSize="" />
            <WordsStyle name="COMMENT DOC KEYWORD ERROR" styleID="18" fgColor="008080" bgColor="FFFFFF" fontName="" fontStyle="0" fontSize="" />
        </LexerType>
        <LexerType name="d" desc="D" ext="">
            <WordsStyle name="DEFAULT" styleID="0" fgColor="000000" bgColor="FFFFFF" fontName="" fontStyle="0" fontSize="" />
            <WordsStyle name="IDENTIFIER" styleID="14" fgColor="000000" bgColor="FFFFFF" fontName="" fontStyle="0" fontSize="" />
            <WordsStyle name="INSTRUCTION WORD" styleID="6" fgColor="0000FF" bgColor="FFFFFF" fontName="" fontStyle="1" fontSize="" keywordClass="instre1" />
            <WordsStyle name="KEWORD1" styleID="7" fgColor="000000" bgColor="FFFFFF" fontName="" fontStyle="0" fontSize="" keywordClass="instre2"/>
            <WordsStyle name="KEWORD2" styleID="8" fgColor="000000" bgColor="FFFFFF" fontName="" fontStyle="0" fontSize="" keywordClass="type1"/>
            <WordsStyle name="KEWORD3" styleID="9" fgColor="000000" bgColor="FFFFFF" fontName="" fontStyle="0" fontSize="" keywordClass="type2"/>
            <WordsStyle name="KEWORD4" styleID="20" fgColor="000000" bgColor="FFFFFF" fontName="" fontStyle="0" fontSize="" keywordClass="type3"/>
            <WordsStyle name="KEWORD5" styleID="21" fgColor="000000" bgColor="FFFFFF" fontName="" fontStyle="0" fontSize="" keywordClass="type4"/>
            <WordsStyle name="KEWORD6" styleID="22" fgColor="000000" bgColor="FFFFFF" fontName="" fontStyle="0" fontSize="" keywordClass="type5"/>
            <WordsStyle name="NUMBER" styleID="5" fgColor="FF8000" bgColor="FFFFFF" fontName="" fontStyle="0" fontSize="" />
            <WordsStyle name="STRING" styleID="10" fgColor="808080" bgColor="FFFFFF" fontName="" fontStyle="0" fontSize="" />
            <WordsStyle name="CHARACTER" styleID="12" fgColor="808080" bgColor="FFFFFF" fontName="" fontStyle="0" fontSize="" />
            <WordsStyle name="OPERATOR" styleID="13" fgColor="000080" bgColor="FFFFFF" fontName="" fontStyle="1" fontSize="" />
            <WordsStyle name="COMMENT" styleID="1" fgColor="008000" bgColor="FFFFFF" fontName="" fontStyle="0" fontSize="" />
            <WordsStyle name="COMMENT LINE" styleID="2" fgColor="008000" bgColor="FFFFFF" fontName="" fontStyle="0" fontSize="" />
            <WordsStyle name="COMMENT DOC" styleID="3" fgColor="008080" bgColor="FFFFFF" fontName="" fontStyle="0" fontSize="" />
            <WordsStyle name="COMMENT NESTED" styleID="4" fgColor="008080" bgColor="FFFFFF" fontName="" fontStyle="0" fontSize="" />
            <WordsStyle name="COMMENT LINE DOC" styleID="15" fgColor="008080" bgColor="FFFFFF" fontName="" fontStyle="0" fontSize="" />
            <WordsStyle name="COMMENT DOC KEYWORD" styleID="16" fgColor="008080" bgColor="FFFFFF" fontName="" fontStyle="1" fontSize="" />
            <WordsStyle name="COMMENT DOC KEYWORD ERROR" styleID="17" fgColor="008080" bgColor="FFFFFF" fontName="" fontStyle="0" fontSize="" />
        </LexerType>
        <LexerType name="diff" desc="DIFF" ext="">
            <WordsStyle name="DEFAULT" styleID="0" fgColor="000000" bgColor="FFFFFF" fontName="" fontStyle="0" fontSize="" />
            <WordsStyle name="COMMENT" styleID="1" fgColor="008000" bgColor="FFFFFF" fontName="" fontStyle="0" fontSize="" />
            <WordsStyle name="COMMAND" styleID="2" fgColor="0000FF" bgColor="FFFFFF" fontName="" fontStyle="1" fontSize="" />
            <WordsStyle name="HEADER" styleID="3" fgColor="8000FF" bgColor="FFFFFF" fontName="" fontStyle="0" fontSize="" />
            <WordsStyle name="POSITION" styleID="4" fgColor="FF8000" bgColor="FFFFFF" fontName="" fontStyle="0" fontSize="" />
            <WordsStyle name="DELETED" styleID="5" fgColor="808040" bgColor="FFFFFF" fontName="" fontStyle="0" fontSize="" />
            <WordsStyle name="ADDED" styleID="6" fgColor="0080FF" bgColor="FFFFFF" fontName="" fontStyle="0" fontSize="" />
        </LexerType>
        <LexerType name="gui4cli" desc="GUI4CLI" ext="">
            <WordsStyle name="DEFAULT" styleID="0" fgColor="000000" bgColor="FFFFFF" fontName="" fontStyle="0" fontSize="" />
            <WordsStyle name="COMMENT LINE" styleID="1" fgColor="008000" bgColor="FFFFFF" fontName="" fontStyle="0" fontSize="" />
            <WordsStyle name="COMMENT" styleID="2" fgColor="008000" bgColor="FFFFFF" fontName="" fontStyle="0" fontSize="" />
            <WordsStyle name="GLOBAL" styleID="5" fgColor="0000FF" bgColor="FFFFFF" fontName="" fontStyle="1" fontSize="" keywordClass="instre1" />
            <WordsStyle name="EVENT" styleID="5" fgColor="0000FF" bgColor="FFFFFF" fontName="" fontStyle="1" fontSize="" keywordClass="instre2" />
            <WordsStyle name="ATTRIBUTE" styleID="16" fgColor="8000FF" bgColor="FFFFFF" fontName="" fontStyle="0" fontSize="" keywordClass="type1" />
            <WordsStyle name="CONTROL" styleID="16" fgColor="8000FF" bgColor="FFFFFF" fontName="" fontStyle="0" fontSize="" keywordClass="type2" />
            <WordsStyle name="COMMAND" styleID="16" fgColor="8000FF" bgColor="FFFFFF" fontName="" fontStyle="0" fontSize="" keywordClass="type3" />
            <WordsStyle name="STRING" styleID="6" fgColor="808080" bgColor="FFFFFF" fontName="" fontStyle="0" fontSize="" />
            <WordsStyle name="OPERATOR" styleID="10" fgColor="000080" bgColor="FFFFFF" fontName="" fontStyle="1" fontSize="" />
        </LexerType>
        <LexerType name="nfo" desc="Dos Style" ext="">
            <WordsStyle name="DEFAULT" styleID="32" fgColor="2E2E2E" bgColor="FFFFFF" />
        </LexerType>
        <LexerType name="fortran" desc="Fortran" ext="">
            <WordsStyle name="DEFAULT" styleID="0" fgColor="000000" bgColor="FFFFFF" fontName="" fontStyle="0" fontSize="" />
            <WordsStyle name="COMMENT" styleID="1" fgColor="008000" bgColor="FFFFFF" fontName="" fontStyle="0" fontSize="" />
            <WordsStyle name="NUMBER" styleID="2" fgColor="FF8000" bgColor="FFFFFF" fontName="" fontStyle="0" fontSize="" />
            <WordsStyle name="STRING" styleID="3" fgColor="808080" bgColor="FFFFFF" fontName="" fontStyle="0" fontSize="" />
            <WordsStyle name="STRING2" styleID="4" fgColor="808080" bgColor="FFFFFF" fontName="" fontStyle="1" fontSize="" />
            <WordsStyle name="OPERATOR" styleID="6" fgColor="000080" bgColor="FFFFFF" fontName="" fontStyle="1" fontSize="" />
            <WordsStyle name="IDENTIFIER" styleID="7" fgColor="000000" bgColor="FFFFFF" fontName="" fontStyle="0" fontSize="" />
            <WordsStyle name="INSTRUCTION WORD" styleID="8" fgColor="0000FF" bgColor="FFFFFF" fontName="" fontStyle="1" fontSize="" keywordClass="instre1" />
            <WordsStyle name="FUNCTION1" styleID="9" fgColor="8000FF" bgColor="FFFFFF" fontName="" fontStyle="1" fontSize="" keywordClass="instre2" />
            <WordsStyle name="FUNCTION2" styleID="10" fgColor="0080C0" bgColor="FFFFFF" fontName="" fontStyle="1" fontSize="" keywordClass="type1" />
            <WordsStyle name="PREPROCESSOR" styleID="11" fgColor="800000" bgColor="FFFFFF" fontName="" fontStyle="0" fontSize="" />
            <WordsStyle name="OPERATOR2" styleID="12" fgColor="808080" bgColor="FFFFFF" fontName="" fontStyle="0" fontSize="" />
            <WordsStyle name="LABEL" styleID="13" fgColor="FFFFFF" bgColor="FF80FF" fontName="" fontStyle="1" fontSize="" />
            <WordsStyle name="CONTINUATION" styleID="14" fgColor="008000" bgColor="FFFFFF" fontName="" fontStyle="0" fontSize="" />
        </LexerType>
        <LexerType name="haskell" desc="Haskell" ext="">
            <WordsStyle name="DEFAULT" styleID="0" fgColor="000000" bgColor="FFFFFF" fontName="" fontStyle="0" fontSize="" />
            <WordsStyle name="IDENTIFIER" styleID="1" fgColor="000000" bgColor="FFFFFF" fontName="" fontStyle="0" fontSize="" />
            <WordsStyle name="KEYWORD" styleID="2" fgColor="0000FF" bgColor="FFFFFF" fontName="" fontStyle="1" fontSize="" />
            <WordsStyle name="NUMBER" styleID="3" fgColor="800080" bgColor="FFFFFF" fontName="" fontStyle="0" fontSize="" />
            <WordsStyle name="STRING" styleID="4" fgColor="CA6500" bgColor="FFFFFF" fontName="" fontStyle="0" fontSize="" />
            <WordsStyle name="CHARACTER" styleID="5" fgColor="CA6500" bgColor="FFFFFF" fontName="" fontStyle="0" fontSize="" />
            <WordsStyle name="CLASS" styleID="6" fgColor="000000" bgColor="FFFFFF" fontName="" fontStyle="1" fontSize="" />
            <WordsStyle name="MODULE" styleID="7" fgColor="000000" bgColor="FFFFFF" fontName="" fontStyle="0" fontSize="" />
            <WordsStyle name="CAPITAL" styleID="8" fgColor="000000" bgColor="FFFFFF" fontName="" fontStyle="0" fontSize="" />
            <WordsStyle name="DATA" styleID="9" fgColor="000000" bgColor="FFFFFF" fontName="" fontStyle="0" fontSize="" />
            <WordsStyle name="IMPORT" styleID="10" fgColor="000000" bgColor="FFFFFF" fontName="" fontStyle="0" fontSize="" />
            <WordsStyle name="OPERATOR" styleID="11" fgColor="000080" bgColor="FFFFFF" fontName="" fontStyle="0" fontSize="" />
            <WordsStyle name="INSTANCE" styleID="12" fgColor="000000" bgColor="FFFFFF" fontName="" fontStyle="0" fontSize="" />
            <WordsStyle name="COMMENTLINE" styleID="13" fgColor="008000" bgColor="FFFFFF" fontName="" fontStyle="0" fontSize="" />
            <WordsStyle name="COMMENTBLOCK" styleID="14" fgColor="008000" bgColor="FFFFFF" fontName="" fontStyle="0" fontSize="" />
            <WordsStyle name="COMMENTBLOCK2" styleID="15" fgColor="008000" bgColor="FFFFFF" fontName="" fontStyle="0" fontSize="" />
            <WordsStyle name="COMMENTBLOCK3" styleID="16" fgColor="008000" bgColor="FFFFFF" fontName="" fontStyle="0" fontSize="" />
        </LexerType>
        <LexerType name="html" desc="HTML" ext="">
            <WordsStyle name="DEFAULT" styleID="0" fgColor="000000" bgColor="FFFFFF" fontName="" fontStyle="1" fontSize="" />
            <WordsStyle name="COMMENT" styleID="9" fgColor="008000" bgColor="FFFFFF" fontName="" fontStyle="0" fontSize="" />
            <WordsStyle name="NUMBER" styleID="5" fgColor="FF0000" bgColor="FFFFFF" fontName="" fontStyle="0" fontSize="" />
            <WordsStyle name="DOUBLESTRING" styleID="6" fgColor="8000FF" bgColor="FFFFFF" fontName="" fontStyle="1" fontSize="" />
            <WordsStyle name="SINGLESTRING" styleID="7" fgColor="8000FF" bgColor="FFFFFF" fontName="" fontStyle="1" fontSize="" />
            <WordsStyle name="TAG" styleID="1" fgColor="0000FF" bgColor="FFFFFF" fontName="" fontStyle="0" fontSize="" />
            <WordsStyle name="TAGEND" styleID="11" fgColor="0000FF" bgColor="FFFFFF" fontName="" fontStyle="0" fontSize="" />
            <WordsStyle name="TAGUNKNOWN" styleID="2" fgColor="000000" bgColor="FFFFFF" fontName="" fontStyle="0" fontSize="" />
            <WordsStyle name="ATTRIBUTE" styleID="3" fgColor="FF0000" bgColor="FFFFFF" fontName="" fontStyle="0" fontSize="" />
            <WordsStyle name="ATTRIBUTEUNKNOWN" styleID="4" fgColor="000000" bgColor="FFFFFF" fontName="" fontStyle="0" fontSize="" />
            <WordsStyle name="SGMLDEFAULT" styleID="21" fgColor="000000" bgColor="A6CAF0" fontName="" fontStyle="0" fontSize="" />
            <WordsStyle name="CDATA" styleID="17" fgColor="FF8000" bgColor="FFFFFF" fontName="" fontStyle="0" fontSize="" />
            <WordsStyle name="VALUE" styleID="19" fgColor="FF8000" bgColor="FEFDE0" fontName="" fontStyle="0" fontSize="" />
            <WordsStyle name="ENTITY" styleID="10" fgColor="000000" bgColor="FEFDE0" fontName="" fontStyle="2" fontSize="" />
        </LexerType>
        <LexerType name="ini" desc="ini file" ext="">
            <WordsStyle name="DEFAULT" styleID="0" fgColor="000000" bgColor="FFFFFF" fontName="" fontStyle="0" fontSize="" />
            <WordsStyle name="COMMENT" styleID="1" fgColor="008000" bgColor="FFFFFF" fontName="" fontStyle="0" fontSize="" />
            <WordsStyle name="SECTION" styleID="2" fgColor="8000FF" bgColor="F2F4FF" fontName="" fontStyle="1" fontSize="" />
            <WordsStyle name="ASSIGNMENT" styleID="3" fgColor="FF0000" bgColor="FFFFFF" fontName="" fontStyle="1" fontSize="" />
            <WordsStyle name="DEFVAL" styleID="4" fgColor="FF0000" bgColor="FFFFFF" fontName="" fontStyle="0" fontSize="" />
        </LexerType>
        <LexerType name="inno" desc="InnoSetup" ext="">
            <WordsStyle name="DEFAULT" styleID="0" fgColor="000000" bgColor="FFFFFF" fontName="" fontStyle="0" fontSize="" />
            <WordsStyle name="COMMENT" styleID="1" fgColor="008000" bgColor="FFFFFF" fontName="" fontStyle="0" fontSize="" />
            <WordsStyle name="KEYWORD" styleID="2" fgColor="0000FF" bgColor="FFFFFF" fontName="" fontStyle="1" fontSize="" keywordClass="instre2" />
            <WordsStyle name="PARAMETER" styleID="3" fgColor="FF8000" bgColor="FFFFFF" fontName="" fontStyle="1" fontSize="" keywordClass="type1" />
            <WordsStyle name="SECTION" styleID="4" fgColor="000080" bgColor="FFFFFF" fontName="" fontStyle="1" fontSize="" keywordClass="instre1" />
            <WordsStyle name="PREPROCESSOR" styleID="5" fgColor="800000" bgColor="FFFFFF" fontName="" fontStyle="1" fontSize="" keywordClass="type2" />
            <WordsStyle name="PREPROCESSOR INLINE" styleID="6" fgColor="0000FF" bgColor="FFFFFF" fontName="" fontStyle="1" fontSize="" />
            <WordsStyle name="COMMENT PASCAL" styleID="7" fgColor="008080" bgColor="FFFFFF" fontName="" fontStyle="0" fontSize="" />
            <WordsStyle name="KEYWORD PASCAL" styleID="8" fgColor="0080C0" bgColor="FFFFFF" fontName="" fontStyle="1" fontSize="" keywordClass="type3" />
            <WordsStyle name="KEYWORD USER" styleID="9" fgColor="8080FF" bgColor="FFFFCC" fontName="" fontStyle="1" fontSize="" keywordClass="type4" />
            <WordsStyle name="STRING DOUBLE" styleID="10" fgColor="808080" bgColor="FFFFFF" fontName="" fontStyle="0" fontSize="" />
            <WordsStyle name="STRING SINGLE" styleID="11" fgColor="808080" bgColor="FFFFFF" fontName="" fontStyle="0" fontSize="" />
            <WordsStyle name="IDENTIFIER" styleID="12" fgColor="000000" bgColor="FFFFFF" fontName="" fontStyle="0" fontSize="" />
        </LexerType>
        <LexerType name="java" desc="Java" ext="">
            <WordsStyle name="PREPROCESSOR" styleID="9" fgColor="804000" bgColor="FFFFFF" fontName="" fontStyle="0" fontSize="" />
            <WordsStyle name="DEFAULT" styleID="11" fgColor="000000" bgColor="FFFFFF" fontName="" fontStyle="0" fontSize="" />
            <WordsStyle name="INSTRUCTION WORD" styleID="5" fgColor="0000FF" bgColor="FFFFFF" fontName="" fontStyle="1" fontSize="" keywordClass="instre1" />
            <WordsStyle name="TYPE WORD" styleID="16" fgColor="8000FF" bgColor="FFFFFF" fontName="" fontStyle="0" fontSize="" keywordClass="type1" />
            <WordsStyle name="NUMBER" styleID="4" fgColor="FF8000" bgColor="FFFFFF" fontName="" fontStyle="0" fontSize="" />
            <WordsStyle name="STRING" styleID="6" fgColor="808080" bgColor="FFFFFF" fontName="" fontStyle="0" fontSize="" />
            <WordsStyle name="CHARACTER" styleID="7" fgColor="808080" bgColor="FFFFFF" fontName="" fontStyle="0" fontSize="" />
            <WordsStyle name="OPERATOR" styleID="10" fgColor="000080" bgColor="FFFFFF" fontName="" fontStyle="1" fontSize="" />
            <WordsStyle name="VERBATIM" styleID="13" fgColor="000000" bgColor="FFFFFF" fontName="" fontStyle="0" fontSize="" />
            <WordsStyle name="REGEX" styleID="14" fgColor="000000" bgColor="FFFFFF" fontName="" fontStyle="1" fontSize="" />
            <WordsStyle name="COMMENT" styleID="1" fgColor="008000" bgColor="FFFFFF" fontName="" fontStyle="0" fontSize="" />
            <WordsStyle name="COMMENT LINE" styleID="2" fgColor="008000" bgColor="FFFFFF" fontName="" fontStyle="0" fontSize="" />
            <WordsStyle name="COMMENT DOC" styleID="3" fgColor="008080" bgColor="FFFFFF" fontName="" fontStyle="0" fontSize="" />
            <WordsStyle name="COMMENT LINE DOC" styleID="15" fgColor="008080" bgColor="FFFFFF" fontName="" fontStyle="0" fontSize="" />
            <WordsStyle name="COMMENT DOC KEYWORD" styleID="17" fgColor="008080" bgColor="FFFFFF" fontName="" fontStyle="1" fontSize="" />
            <WordsStyle name="COMMENT DOC KEYWORD ERROR" styleID="18" fgColor="008080" bgColor="FFFFFF" fontName="" fontStyle="0" fontSize="" />
        </LexerType>
        <LexerType name="javascript" desc="JavaScript" ext="">
            <WordsStyle name="DEFAULT" styleID="41" fgColor="000000" bgColor="F2F4FF" fontName="" fontStyle="0" fontSize="" />
            <WordsStyle name="NUMBER" styleID="45" fgColor="FF0000" bgColor="F2F4FF" fontName="" fontStyle="0" fontSize="" />
            <WordsStyle name="WORD" styleID="46" fgColor="000000" bgColor="F2F4FF" fontName="" fontStyle="0" fontSize="" />
            <WordsStyle name="KEYWORD" styleID="47" fgColor="000080" bgColor="F2F4FF" fontName="" fontStyle="3" fontSize="" keywordClass="instre1" />
            <WordsStyle name="DOUBLESTRING" styleID="48" fgColor="808080" bgColor="F2F4FF" fontName="" fontStyle="0" fontSize="" />
            <WordsStyle name="SINGLESTRING" styleID="49" fgColor="808080" bgColor="F2F4FF" fontName="" fontStyle="0" fontSize="" />
            <WordsStyle name="SYMBOLS" styleID="50" fgColor="000000" bgColor="F2F4FF" fontName="" fontStyle="1" fontSize="" />
            <WordsStyle name="REGEX" styleID="52" fgColor="8000FF" bgColor="F2F4FF" fontName="" fontStyle="0" fontSize="" />
            <WordsStyle name="COMMENT" styleID="42" fgColor="008000" bgColor="F2F4FF" fontName="" fontStyle="0" fontSize="" />
            <WordsStyle name="COMMENTLINE" styleID="43" fgColor="008000" bgColor="F2F4FF" fontName="" fontStyle="0" fontSize="" />
            <WordsStyle name="COMMENTDOC" styleID="44" fgColor="008080" bgColor="F2F4FF" fontName="" fontStyle="0" fontSize="" />
        </LexerType>
        <LexerType name="kix" desc="KiXtart" ext="">
            <WordsStyle name="DEFAULT" styleID="31" fgColor="000000" bgColor="FFFFFF" fontName="" fontStyle="0" fontSize="" />
            <WordsStyle name="COMMENT" styleID="1" fgColor="008000" bgColor="FFFFFF" fontName="" fontStyle="0" fontSize="" />
            <WordsStyle name="STRING" styleID="2" fgColor="808080" bgColor="FFFFFF" fontName="" fontStyle="0" fontSize="" />
            <WordsStyle name="STRING2" styleID="3" fgColor="808080" bgColor="FFFFFF" fontName="" fontStyle="0" fontSize="" />
            <WordsStyle name="NUMBER" styleID="4" fgColor="FF8000" bgColor="FFFFFF" fontName="" fontStyle="0" fontSize="" />
            <WordsStyle name="VAR" styleID="5" fgColor="000000" bgColor="FFFFFF" fontName="" fontStyle="0" fontSize="" />
            <WordsStyle name="MACRO" styleID="6" fgColor="8000FF" bgColor="FFFFFF" fontName="" fontStyle="0" fontSize="" keywordClass="instre2" />
            <WordsStyle name="INSTRUCTION WORD" styleID="7" fgColor="0000FF" bgColor="FFFFFF" fontName="" fontStyle="1" fontSize="" keywordClass="instre1" />
            <WordsStyle name="FUNCTION" styleID="8" fgColor="8000FF" bgColor="FFFFFF" fontName="" fontStyle="0" fontSize="" keywordClass="type1" />
            <WordsStyle name="OPERATOR" styleID="9" fgColor="000080" bgColor="FFFFFF" fontName="" fontStyle="1" fontSize="" />
        </LexerType>
        <LexerType name="lisp" desc="LISP" ext="">
            <WordsStyle name="DEFAULT" styleID="0" fgColor="000000" bgColor="FFFFFF" fontName="" fontStyle="0" fontSize="" />
            <WordsStyle name="COMMENTLINE" styleID="1" fgColor="008000" bgColor="FFFFFF" fontName="" fontStyle="0" fontSize="" />
            <WordsStyle name="NUMBER" styleID="2" fgColor="FF8000" bgColor="FFFFFF" fontName="" fontStyle="0" fontSize="" />
            <WordsStyle name="FUNCTION WORD" styleID="3" fgColor="0000FF" bgColor="FFFFFF" fontName="" fontStyle="1" fontSize="" keywordClass="instre1" />
            <WordsStyle name="FUNCTION WORD2" styleID="4" fgColor="0000FF" bgColor="FFFFFF" fontName="" fontStyle="1" fontSize="" keywordClass="instre2" />
            <WordsStyle name="SYMBOL" styleID="5" fgColor="000080" bgColor="FFFFFF" fontName="" fontStyle="1" fontSize="" />
            <WordsStyle name="STRING" styleID="6" fgColor="808080" bgColor="FFFFFF" fontName="" fontStyle="0" fontSize="" />
            <WordsStyle name="IDENTIFIER" styleID="9" fgColor="000000" bgColor="FFFFFF" fontName="" fontStyle="0" fontSize="" />
            <WordsStyle name="OPERATOR" styleID="10" fgColor="0080C0" bgColor="FFFFFF" fontName="" fontStyle="1" fontSize="" keywordClass="type1" />
            <WordsStyle name="SPECIAL" styleID="11" fgColor="800000" bgColor="FFFFFF" fontName="" fontStyle="0" fontSize="" />
            <WordsStyle name="COMMENT" styleID="12" fgColor="808080" bgColor="FFFFFF" fontName="" fontStyle="0" fontSize="" />
        </LexerType>
        <LexerType name="lua" desc="Lua" ext="">
            <WordsStyle name="DEFAULT" styleID="0" fgColor="000000" bgColor="FFFFFF" fontName="" fontStyle="0" fontSize="" />
            <WordsStyle name="COMMENT" styleID="1" fgColor="008000" bgColor="FFFFFF" fontName="" fontStyle="0" fontSize="" />
            <WordsStyle name="COMMENT LINE" styleID="2" fgColor="008000" bgColor="FFFFFF" fontName="" fontStyle="0" fontSize="" />
            <WordsStyle name="COMMENT DOC" styleID="3" fgColor="008080" bgColor="FFFFFF" fontName="" fontStyle="0" fontSize="" />
            <WordsStyle name="LITERALSTRING" styleID="8" fgColor="95004A" bgColor="FFFFFF" fontName="" fontStyle="0" fontSize="" />
            <WordsStyle name="PREPROCESSOR" styleID="9" fgColor="804000" bgColor="FFFFFF" fontName="" fontStyle="0" fontSize="" />
            <WordsStyle name="INSTRUCTION WORD" styleID="5" fgColor="0000FF" bgColor="FFFFFF" fontName="" fontStyle="1" fontSize="" keywordClass="instre1" />
            <WordsStyle name="NUMBER" styleID="4" fgColor="FF8000" bgColor="FFFFFF" fontName="" fontStyle="0" fontSize="" />
            <WordsStyle name="STRING" styleID="6" fgColor="808080" bgColor="FFFFFF" fontName="" fontStyle="0" fontSize="" />
            <WordsStyle name="CHARACTER" styleID="7" fgColor="808080" bgColor="FFFFFF" fontName="" fontStyle="0" fontSize="" />
            <WordsStyle name="OPERATOR" styleID="10" fgColor="000080" bgColor="FFFFFF" fontName="" fontStyle="1" fontSize="" />
            <WordsStyle name="FUNC1" styleID="13" fgColor="0080C0" bgColor="FFFFFF" fontName="" fontStyle="1" fontSize="" keywordClass="instre2" />
            <WordsStyle name="FUNC2" styleID="14" fgColor="8000FF" bgColor="FFFFFF" fontName="" fontStyle="1" fontSize="" keywordClass="type1" />
            <WordsStyle name="FUNC3" styleID="15" fgColor="0000A0" bgColor="FFFFFF" fontName="" fontStyle="3" fontSize="" keywordClass="type2" />
        </LexerType>
        <LexerType name="makefile" desc="Makefile" ext="">
            <WordsStyle name="DEFAULT" styleID="0" fgColor="000000" bgColor="FFFFFF" fontName="" fontStyle="0" fontSize="" />
            <WordsStyle name="COMMENT" styleID="1" fgColor="008000" bgColor="FFFFFF" fontName="" fontStyle="0" fontSize="" />
            <WordsStyle name="PREPROCESSOR" styleID="2" fgColor="FFFF00" bgColor="FFFFFF" fontName="" fontStyle="1" fontSize="" />
            <WordsStyle name="IDENTIFIER" styleID="3" fgColor="0000FF" bgColor="FFFFFF" fontName="" fontStyle="0" fontSize="" />
            <WordsStyle name="OPERATOR" styleID="4" fgColor="000000" bgColor="FFFFFF" fontName="" fontStyle="1" fontSize="" />
            <WordsStyle name="TARGET" styleID="5" fgColor="FF0000" bgColor="FFFFFF" fontName="" fontStyle="0" fontSize="" />
            <WordsStyle name="IDEOL" styleID="9" fgColor="000000" bgColor="FFFFFF" fontName="" fontStyle="2" fontSize="" />
        </LexerType>
        <LexerType name="matlab" desc="Matlab" ext="">
            <WordsStyle name="DEFAULT" styleID="0" fgColor="000000" bgColor="FFFFFF" fontName="" fontStyle="0" fontSize="" />
            <WordsStyle name="COMMENT" styleID="1" fgColor="008000" bgColor="FFFFFF" fontName="" fontStyle="0" fontSize="" />
            <WordsStyle name="COMMAND" styleID="2" fgColor="8000FF" bgColor="FFFFFF" fontName="" fontStyle="0" fontSize="" />
            <WordsStyle name="NUMBER" styleID="3" fgColor="FF8000" bgColor="FFFFFF" fontName="" fontStyle="0" fontSize="" />
            <WordsStyle name="INSTRUCTION WORD" styleID="4" fgColor="0000FF" bgColor="FFFFFF" fontName="" fontStyle="1" fontSize="" keywordClass="instre1" />
            <WordsStyle name="STRING" styleID="5" fgColor="808080" bgColor="FFFFFF" fontName="" fontStyle="0" fontSize="" />
            <WordsStyle name="OPERATOR" styleID="6" fgColor="000080" bgColor="FFFFFF" fontName="" fontStyle="1" fontSize="" />
            <WordsStyle name="IDENTIFIER" styleID="7" fgColor="000000" bgColor="FFFFFF" fontName="" fontStyle="0" fontSize="" />
            <WordsStyle name="DOUBLE QUOTE STRING" styleID="8" fgColor="808080" bgColor="FFFFFF" fontName="" fontStyle="0" fontSize="" />
        </LexerType>
        <LexerType name="nsis" desc="NSIS" ext="">
            <WordsStyle name="DEFAULT" styleID="0" fgColor="000000" bgColor="FFFFFF" fontName="" fontStyle="0" fontSize="" />
            <WordsStyle name="COMMENTLINE" styleID="1" fgColor="008000" bgColor="FFFFFF" fontName="" fontStyle="0" fontSize="" />
            <WordsStyle name="STRING DOUBLE QUOTE" styleID="2" fgColor="808080" bgColor="EEEEEE" fontName="" fontStyle="0" fontSize="" />
            <WordsStyle name="STRING LEFT QUOTE" styleID="3" fgColor="FFFF80" bgColor="C0C0C0" fontName="" fontStyle="0" fontSize="" />
            <WordsStyle name="STRING RIGHT QUOTE" styleID="4" fgColor="FFFFFF" bgColor="C0C0C0" fontName="" fontStyle="0" fontSize="" />
            <WordsStyle name="FUNCTION" styleID="5" fgColor="0000FF" bgColor="FFFFFF" fontName="" fontStyle="0" fontSize="" keywordClass="instre1" />
            <WordsStyle name="VARIABLE" styleID="6" fgColor="FF8000" bgColor="FFFFFF" fontName="" fontStyle="0" fontSize="" keywordClass="instre2" />
            <WordsStyle name="LABEL" styleID="7" fgColor="FF0000" bgColor="FFFF80" fontName="" fontStyle="0" fontSize="" keywordClass="type1" />
            <WordsStyle name="USER DEFINED" styleID="8" fgColor="FDFFEC" bgColor="FF80FF" fontName="" fontStyle="4" fontSize="" keywordClass="type2" />
            <WordsStyle name="SECTION" styleID="9" fgColor="0000FF" bgColor="FFFFFF" fontName="" fontStyle="1" fontSize="" />
            <WordsStyle name="SUBSECTION" styleID="10" fgColor="000000" bgColor="FFFFFF" fontName="" fontStyle="1" fontSize="" />
            <WordsStyle name="IF DEFINE" styleID="11" fgColor="808040" bgColor="FFFFFF" fontName="" fontStyle="0" fontSize="" />
            <WordsStyle name="MACRO" styleID="12" fgColor="800000" bgColor="FFFFFF" fontName="" fontStyle="1" fontSize="" />
            <WordsStyle name="STRING VAR" styleID="13" fgColor="FF8000" bgColor="EFEFEF" fontName="" fontStyle="0" fontSize="" />
            <WordsStyle name="NUMBER" styleID="14" fgColor="FF0000" bgColor="FFFFFF" fontName="" fontStyle="0" fontSize="" />
            <WordsStyle name="SECTION GROUP" styleID="15" fgColor="0000FF" bgColor="FFFFFF" fontName="" fontStyle="1" fontSize="" />
            <WordsStyle name="PAGE EX" styleID="16" fgColor="0000FF" bgColor="FFFFFF" fontName="" fontStyle="1" fontSize="" />
            <WordsStyle name="FUNCTION DEFINITIONS" styleID="17" fgColor="0000FF" bgColor="FFFFFF" fontName="" fontStyle="1" fontSize="" />
            <WordsStyle name="COMMENT" styleID="18" fgColor="008000" bgColor="FFFFFF" fontName="" fontStyle="0" fontSize="" />
        </LexerType>
        <LexerType name="objc" desc="Objective-C" ext="">
            <WordsStyle name="DIRECTIVE" styleID="19" fgColor="A001D6" bgColor="FFFFFF" fontName="" fontStyle="1" fontSize="" keywordClass="instre2" />
            <WordsStyle name="DEFAULT" styleID="11" fgColor="000000" bgColor="FFFFFF" fontName="" fontStyle="0" fontSize="" />
            <WordsStyle name="QUALIFIER" styleID="20" fgColor="95004A" bgColor="FFFFFF" fontName="" fontStyle="0" fontSize="" keywordClass="type2" />
            <WordsStyle name="PREPROCESSOR" styleID="9" fgColor="804000" bgColor="FFFFFF" fontName="" fontStyle="0" fontSize="" />
            <WordsStyle name="INSTRUCTION WORD" styleID="5" fgColor="0000FF" bgColor="FFFFFF" fontName="" fontStyle="1" fontSize="" keywordClass="instre1" />
            <WordsStyle name="TYPE WORD" styleID="16" fgColor="8000FF" bgColor="FFFFFF" fontName="" fontStyle="0" fontSize="" keywordClass="type1" />
            <WordsStyle name="NUMBER" styleID="4" fgColor="FF8000" bgColor="FFFFFF" fontName="" fontStyle="0" fontSize="" />
            <WordsStyle name="STRING" styleID="6" fgColor="808080" bgColor="FFFFFF" fontName="" fontStyle="0" fontSize="" />
            <WordsStyle name="CHARACTER" styleID="7" fgColor="808080" bgColor="FFFFFF" fontName="" fontStyle="0" fontSize="" />
            <WordsStyle name="OPERATOR" styleID="10" fgColor="000080" bgColor="FFFFFF" fontName="" fontStyle="1" fontSize="" />
            <WordsStyle name="VERBATIM" styleID="13" fgColor="808080" bgColor="FFFFFF" fontName="" fontStyle="1" fontSize="" />
            <WordsStyle name="REGEX" styleID="14" fgColor="000000" bgColor="FFFFFF" fontName="" fontStyle="1" fontSize="" />
            <WordsStyle name="COMMENT" styleID="1" fgColor="008000" bgColor="FFFFFF" fontName="" fontStyle="0" fontSize="" />
            <WordsStyle name="COMMENT LINE" styleID="2" fgColor="008000" bgColor="FFFFFF" fontName="" fontStyle="0" fontSize="" />
            <WordsStyle name="COMMENT DOC" styleID="3" fgColor="008080" bgColor="FFFFFF" fontName="" fontStyle="0" fontSize="" />
            <WordsStyle name="COMMENT LINE DOC" styleID="15" fgColor="008080" bgColor="FFFFFF" fontName="" fontStyle="0" fontSize="" />
            <WordsStyle name="COMMENT DOC KEYWORD" styleID="17" fgColor="008080" bgColor="FFFFFF" fontName="" fontStyle="1" fontSize="" />
            <WordsStyle name="COMMENT DOC KEYWORD ERROR" styleID="18" fgColor="008080" bgColor="FFFFFF" fontName="" fontStyle="0" fontSize="" />
        </LexerType>
        <LexerType name="pascal" desc="Pascal" ext="">
            <WordsStyle name="DEFAULT" styleID="0" fgColor="808080" bgColor="FFFFFF" fontName="" fontStyle="0" fontSize="" />
            <WordsStyle name="IDENTIFIER" styleID="1" fgColor="000000" bgColor="FFFFFF" fontName="" fontStyle="0" fontSize="" />
            <WordsStyle name="COMMENT" styleID="2" fgColor="008000" bgColor="FFFFFF" fontName="" fontStyle="0" fontSize="" />
            <WordsStyle name="COMMENT LINE" styleID="3" fgColor="008000" bgColor="FFFFFF" fontName="" fontStyle="0" fontSize="" />
            <WordsStyle name="COMMENT DOC" styleID="4" fgColor="008080" bgColor="FFFFFF" fontName="" fontStyle="0" fontSize="" />
            <WordsStyle name="PREPROCESSOR" styleID="5" fgColor="804000" bgColor="FFFFFF" fontName="" fontStyle="0" fontSize="" />
            <WordsStyle name="PREPROCESSOR2" styleID="6" fgColor="804000" bgColor="FFFFFF" fontName="" fontStyle="0" fontSize="" />
            <WordsStyle name="NUMBER" styleID="7" fgColor="FF8000" bgColor="FFFFFF" fontName="" fontStyle="0" fontSize="" />
            <WordsStyle name="HEX NUMBER" styleID="8" fgColor="FF8000" bgColor="FFFFFF" fontName="" fontStyle="0" fontSize="" />
            <WordsStyle name="INSTRUCTION WORD" styleID="9" fgColor="0000FF" bgColor="FFFFFF" fontName="" fontStyle="1" fontSize="" keywordClass="instre1" />
            <WordsStyle name="STRING" styleID="10" fgColor="808080" bgColor="FFFFFF" fontName="" fontStyle="0" fontSize="" />
            <WordsStyle name="CHARACTER" styleID="12" fgColor="808080" bgColor="FFFFFF" fontName="" fontStyle="0" fontSize="" />
            <WordsStyle name="OPERATOR" styleID="13" fgColor="000080" bgColor="FFFFFF" fontName="" fontStyle="1" fontSize="" />
            <WordsStyle name="ASM" styleID="14" fgColor="000000" bgColor="FFFFFF" fontName="" fontStyle="1" fontSize="" />
        </LexerType>
        <LexerType name="perl" desc="Perl" ext="">
            <WordsStyle name="PREPROCESSOR" styleID="9" fgColor="804000" bgColor="FFFFFF" fontName="" fontStyle="0" fontSize="" />
            <WordsStyle name="DEFAULT" styleID="0" fgColor="FF0000" bgColor="FFFFFF" fontName="" fontStyle="0" fontSize="" />
            <WordsStyle name="INSTRUCTION WORD" styleID="5" fgColor="0000FF" bgColor="FFFFFF" fontName="" fontStyle="1" fontSize="" keywordClass="instre1" />
            <WordsStyle name="NUMBER" styleID="4" fgColor="FF0000" bgColor="FFFFFF" fontName="" fontStyle="0" fontSize="" />
            <WordsStyle name="STRING" styleID="6" fgColor="808080" bgColor="FFFFFF" fontName="" fontStyle="0" fontSize="" />
            <WordsStyle name="CHARACTER" styleID="7" fgColor="808080" bgColor="FFFFFF" fontName="" fontStyle="0" fontSize="" />
            <WordsStyle name="OPERATOR" styleID="10" fgColor="000080" bgColor="FFFFFF" fontName="" fontStyle="1" fontSize="" />
            <WordsStyle name="REGEX" styleID="17" fgColor="8080FF" bgColor="F8FEDE" fontName="" fontStyle="0" fontSize="" />
            <WordsStyle name="COMMENT LINE" styleID="2" fgColor="008000" bgColor="FFFFFF" fontName="" fontStyle="0" fontSize="" />
            <WordsStyle name="SCALAR" styleID="12" fgColor="FF8000" bgColor="FFFFFF" fontName="" fontStyle="0" fontSize="" />
            <WordsStyle name="ARRAY" styleID="13" fgColor="CF34CF" bgColor="FFFFFF" fontName="" fontStyle="0" fontSize="" />
            <WordsStyle name="HASH" styleID="14" fgColor="8080C0" bgColor="FFFFFF" fontName="" fontStyle="0" fontSize="" />
            <WordsStyle name="SYMBOL TABLE" styleID="15" fgColor="FF0000" bgColor="FFFFFF" fontName="" fontStyle="1" fontSize="" />
            <WordsStyle name="PUNCTUATION" styleID="8" fgColor="804000" bgColor="FFFFFF" fontName="" fontStyle="0" fontSize="" />
            <WordsStyle name="POD" styleID="3" fgColor="000000" bgColor="FFFFFF" fontName="" fontStyle="0" fontSize="" />
            <WordsStyle name="ERROR" styleID="1" fgColor="FF80C0" bgColor="FFFFFF" fontName="" fontStyle="3" fontSize="" />
            <WordsStyle name="LONGQUOTE" styleID="19" fgColor="FF8000" bgColor="FFFFFF" fontName="" fontStyle="0" fontSize="" />
            <WordsStyle name="DATASECTION" styleID="21" fgColor="808080" bgColor="FFFFFF" fontName="" fontStyle="0" fontSize="" />
            <WordsStyle name="REGSUBST" styleID="18" fgColor="8080C0" bgColor="FFEEEC" fontName="" fontStyle="0" fontSize="" />
            <WordsStyle name="BACKTICKS" styleID="20" fgColor="FFFF00" bgColor="808080" fontName="" fontStyle="1" fontSize="" />
        </LexerType>
        <LexerType name="php" desc="php" ext="">
            <WordsStyle name="QUESTION MARK" styleID="18" fgColor="FF0000" bgColor="FDF8E3" fontName="" fontStyle="0" fontSize="" />
            <WordsStyle name="DEFAULT" styleID="118" fgColor="000000" bgColor="FEFCF5" fontName="" fontStyle="0" fontSize="" />
            <WordsStyle name="STRING" styleID="119" fgColor="808080" bgColor="FEFCF5" fontName="" fontStyle="0" fontSize="" />
            <WordsStyle name="STRING VARIABLE" styleID="126" fgColor="808080" bgColor="FEFCF5" fontName="" fontStyle="1" fontSize="" />
            <WordsStyle name="SIMPLESTRING" styleID="120" fgColor="808080" bgColor="FEFCF5" fontName="" fontStyle="0" fontSize="" />
            <WordsStyle name="WORD" styleID="121" fgColor="0000FF" bgColor="FEFCF5" fontName="" fontStyle="1" fontSize="" keywordClass="instre1" />
            <WordsStyle name="NUMBER" styleID="122" fgColor="FF8000" bgColor="FEFCF5" fontName="" fontStyle="0" fontSize="" />
            <WordsStyle name="VARIABLE" styleID="123" fgColor="000080" bgColor="FEFCF5" fontName="" fontStyle="0" fontSize="" />
            <WordsStyle name="COMMENT" styleID="124" fgColor="008000" bgColor="FEFCF5" fontName="" fontStyle="0" fontSize="" />
            <WordsStyle name="COMMENTLINE" styleID="125" fgColor="008000" bgColor="FEFCF5" fontName="" fontStyle="0" fontSize="" />
            <WordsStyle name="OPERATOR" styleID="127" fgColor="8000FF" bgColor="FEFCF5" fontName="" fontStyle="0" fontSize="" />
        </LexerType>
        <LexerType name="postscript" desc="Postscript" ext="">
            <WordsStyle name="DEFAULT" styleID="0" fgColor="000000" bgColor="FFFFFF" fontName="" fontStyle="0" fontSize="" />
            <WordsStyle name="COMMENT" styleID="1" fgColor="008000" bgColor="FFFFFF" fontName="" fontStyle="0" fontSize="" />
            <WordsStyle name="DSC COMMENT" styleID="2" fgColor="008000" bgColor="FFFFFF" fontName="" fontStyle="0" fontSize="" />
            <WordsStyle name="DSC VALUE" styleID="3" fgColor="FF0000" bgColor="FFFFFF" fontName="" fontStyle="0" fontSize="" />
            <WordsStyle name="NUMBER" styleID="4" fgColor="FF8000" bgColor="FFFFFF" fontName="" fontStyle="0" fontSize="" />
            <WordsStyle name="Name" styleID="5" fgColor="000000" bgColor="FFFFFF" fontName="" fontStyle="0" fontSize="" />
            <WordsStyle name="INSTRUCTION" styleID="6" fgColor="0000FF" bgColor="FFFFFF" fontName="" fontStyle="1" fontSize="" keywordClass="instre1" />
            <WordsStyle name="LITERAL" styleID="7" fgColor="0080C0" bgColor="FFFFFF" fontName="" fontStyle="1" fontSize="" />
            <WordsStyle name="IMMEVAL" styleID="8" fgColor="000080" bgColor="FFFFFF" fontName="" fontStyle="1" fontSize="" />
            <WordsStyle name="PAREN ARRAY" styleID="9" fgColor="FF00FF" bgColor="FFFFFF" fontName="" fontStyle="1" fontSize="" />
            <WordsStyle name="PAREN DICT" styleID="10" fgColor="0080FF" bgColor="FFFFFF" fontName="" fontStyle="1" fontSize="" />
            <WordsStyle name="PAREN PROC" styleID="11" fgColor="000080" bgColor="FFFFFF" fontName="" fontStyle="1" fontSize="" />
            <WordsStyle name="TEXT" styleID="12" fgColor="808000" bgColor="FFFFFF" fontName="" fontStyle="0" fontSize="" />
            <WordsStyle name="HEX STRING" styleID="13" fgColor="808080" bgColor="FFFFFF" fontName="" fontStyle="0" fontSize="" />
            <WordsStyle name="BASE85 STRING" styleID="14" fgColor="808080" bgColor="FFFFFF" fontName="" fontStyle="0" fontSize="" />
            <WordsStyle name="BAD STRING CHAR" styleID="15" fgColor="804000" bgColor="FFFFFF" fontName="" fontStyle="1" fontSize="" />
        </LexerType>
        <LexerType name="POV" desc="POV" ext="">
            <WordsStyle name="DEFAULT" styleID="0" fgColor="000000" bgColor="FFFFFF" fontName="" fontStyle="0" fontSize="" />
            <WordsStyle name="COMMENT" styleID="1" fgColor="008000" bgColor="FFFFFF" fontName="" fontStyle="0" fontSize="" />
            <WordsStyle name="DSC COMMENT" styleID="2" fgColor="008000" bgColor="FFFFFF" fontName="" fontStyle="0" fontSize="" />
            <WordsStyle name="DSC VALUE" styleID="3" fgColor="FF0000" bgColor="FFFFFF" fontName="" fontStyle="0" fontSize="" />
            <WordsStyle name="NUMBER" styleID="4" fgColor="FF8000" bgColor="FFFFFF" fontName="" fontStyle="0" fontSize="" />
            <WordsStyle name="Name" styleID="5" fgColor="000000" bgColor="FFFFFF" fontName="" fontStyle="0" fontSize="" />
            <WordsStyle name="INSTRUCTION" styleID="6" fgColor="0000FF" bgColor="FFFFFF" fontName="" fontStyle="1" fontSize="" keywordClass="instre1" />
            <WordsStyle name="LITERAL" styleID="7" fgColor="0080C0" bgColor="FFFFFF" fontName="" fontStyle="1" fontSize="" />
            <WordsStyle name="IMMEVAL" styleID="8" fgColor="000080" bgColor="FFFFFF" fontName="" fontStyle="1" fontSize="" />
            <WordsStyle name="PAREN ARRAY" styleID="9" fgColor="FF00FF" bgColor="FFFFFF" fontName="" fontStyle="1" fontSize="" />
            <WordsStyle name="PAREN DICT" styleID="10" fgColor="0080FF" bgColor="FFFFFF" fontName="" fontStyle="1" fontSize="" />
            <WordsStyle name="PAREN PROC" styleID="11" fgColor="000080" bgColor="FFFFFF" fontName="" fontStyle="1" fontSize="" />
            <WordsStyle name="TEXT" styleID="12" fgColor="808000" bgColor="FFFFFF" fontName="" fontStyle="0" fontSize="" />
            <WordsStyle name="HEX STRING" styleID="13" fgColor="808080" bgColor="FFFFFF" fontName="" fontStyle="0" fontSize="" />
            <WordsStyle name="BASE85 STRING" styleID="14" fgColor="808080" bgColor="FFFFFF" fontName="" fontStyle="0" fontSize="" />
            <WordsStyle name="BAD STRING CHAR" styleID="15" fgColor="804000" bgColor="FFFFFF" fontName="" fontStyle="1" fontSize="" />
        </LexerType>
        <LexerType name="powershell" desc="PowerShell" ext="">
            <WordsStyle name="DEFAULT" styleID="0" fgColor="000000" bgColor="FFFFFF" fontName="" fontStyle="0" fontSize="" />
            <WordsStyle name="COMMENT" styleID="1" fgColor="008000" bgColor="FFFFFF" fontName="" fontStyle="0" fontSize="" />
            <WordsStyle name="STRING" styleID="2" fgColor="808080" bgColor="FFFFFF" fontName="" fontStyle="0" fontSize="" />
            <WordsStyle name="CHARACTER" styleID="3" fgColor="808080" bgColor="FFFFFF" fontName="" fontStyle="0" fontSize="" />
            <WordsStyle name="NUMBER" styleID="4" fgColor="FF8000" bgColor="FFFFFF" fontName="" fontStyle="0" fontSize="" />
            <WordsStyle name="VARIABLE" styleID="5" fgColor="000000" bgColor="FFFFFF" fontName="" fontStyle="1" fontSize="" />
            <WordsStyle name="OPERATOR" styleID="6" fgColor="000080" bgColor="FFFFFF" fontName="" fontStyle="1" fontSize="" />
            <WordsStyle name="INSTRUCTION WORD" styleID="8" fgColor="0000FF" bgColor="FFFFFF" fontName="" fontStyle="1" fontSize="" keywordClass="instre1" />
            <WordsStyle name="CMDLET" styleID="9" fgColor="8000FF" bgColor="FFFFFF" fontName="" fontStyle="0" fontSize="" keywordClass="instre2" />
            <WordsStyle name="ALIAS" styleID="10" fgColor="0080FF" bgColor="FFFFFF" fontName="" fontStyle="0" fontSize="" keywordClass="type1" />
        </LexerType>
        <LexerType name="props" desc="Properties file" ext="">
            <WordsStyle name="DEFAULT" styleID="0" fgColor="000000" bgColor="FFFFFF" fontName="" fontStyle="0" fontSize="" />
            <WordsStyle name="COMMENT" styleID="1" fgColor="008000" bgColor="FFFFFF" fontName="" fontStyle="0" fontSize="" />
            <WordsStyle name="SECTION" styleID="2" fgColor="8000FF" bgColor="F2F4FF" fontName="" fontStyle="1" fontSize="" />
            <WordsStyle name="ASSIGNMENT" styleID="3" fgColor="FF0000" bgColor="FFFFFF" fontName="" fontStyle="1" fontSize="" />
            <WordsStyle name="DEFVAL" styleID="4" fgColor="FF0000" bgColor="FFFFFF" fontName="" fontStyle="0" fontSize="" />
        </LexerType>
        <LexerType name="python" desc="Python" ext="">
            <WordsStyle name="DEFAULT" styleID="0" fgColor="000000" bgColor="FFFFFF" fontName="" fontStyle="0" fontSize="" />
            <WordsStyle name="COMMENTLINE" styleID="1" fgColor="008000" bgColor="FFFFFF" fontName="" fontStyle="0" fontSize="" />
            <WordsStyle name="NUMBER" styleID="2" fgColor="FF0000" bgColor="FFFFFF" fontName="" fontStyle="0" fontSize="" />
            <WordsStyle name="STRING" styleID="3" fgColor="808080" bgColor="FFFFFF" fontName="" fontStyle="0" fontSize="" />
            <WordsStyle name="CHARACTER" styleID="4" fgColor="808080" bgColor="FFFFFF" fontName="" fontStyle="0" fontSize="" />
            <WordsStyle name="KEYWORDS" styleID="5" fgColor="0000FF" bgColor="FFFFFF" fontName="" fontStyle="1" fontSize="" keywordClass="instre1" />
            <WordsStyle name="TRIPLE" styleID="6" fgColor="FF8000" bgColor="FFFFFF" fontName="" fontStyle="0" fontSize="" />
            <WordsStyle name="TRIPLEDOUBLE" styleID="7" fgColor="000000" bgColor="FFFFFF" fontName="" fontStyle="0" fontSize="" />
            <WordsStyle name="CLASSNAME" styleID="8" fgColor="000000" bgColor="FFFFFF" fontName="" fontStyle="1" fontSize="" />
            <WordsStyle name="DEFNAME" styleID="9" fgColor="FF00FF" bgColor="FFFFFF" fontName="" fontStyle="0" fontSize="" />
            <WordsStyle name="OPERATOR" styleID="10" fgColor="000080" bgColor="FFFFFF" fontName="" fontStyle="1" fontSize="" />
            <WordsStyle name="IDENTIFIER" styleID="11" fgColor="000000" bgColor="FFFFFF" fontName="" fontStyle="0" fontSize="" />
            <WordsStyle name="COMMENTBLOCK" styleID="12" fgColor="008000" bgColor="FFFFFF" fontName="" fontStyle="0" fontSize="" />
        </LexerType>
        <LexerType name="r" desc="R" ext="">
            <WordsStyle name="DEFAULT" styleID="0" fgColor="000000" bgColor="FFFFFF" fontName="" fontStyle="0" fontSize="" />
            <WordsStyle name="COMMENT" styleID="1" fgColor="008000" bgColor="FFFFFF" fontName="" fontStyle="0" fontSize="" />
            <WordsStyle name="INSTRUCTION WORD" styleID="2" fgColor="0000FF" bgColor="FFFFFF" fontName="" fontStyle="1" fontSize="" keywordClass="instre1" />
            <WordsStyle name="BASE WORD" styleID="3" fgColor="8000FF" bgColor="FFFFFF" fontName="" fontStyle="0" fontSize="" keywordClass="instre2" />
            <WordsStyle name="KEYWORD" styleID="4" fgColor="0080FF" bgColor="FFFFFF" fontName="" fontStyle="0" fontSize="" keywordClass="type1" />
            <WordsStyle name="NUMBER" styleID="5" fgColor="FF8000" bgColor="FFFFFF" fontName="" fontStyle="0" fontSize="" />
            <WordsStyle name="STRING" styleID="6" fgColor="808080" bgColor="FFFFFF" fontName="" fontStyle="0" fontSize="" />
            <WordsStyle name="STRING2" styleID="7" fgColor="808080" bgColor="FFFFFF" fontName="" fontStyle="0" fontSize="" />
            <WordsStyle name="OPERATOR" styleID="8" fgColor="000080" bgColor="FFFFFF" fontName="" fontStyle="1" fontSize="" />
            <WordsStyle name="INFIX" styleID="10" fgColor="804000" bgColor="FFFFFF" fontName="" fontStyle="0" fontSize="" />
        </LexerType>
        <LexerType name="rc" desc="RC" ext="">
            <WordsStyle name="PREPROCESSOR" styleID="9" fgColor="804000" bgColor="FFFFFF" fontName="" fontStyle="0" fontSize="" />
            <WordsStyle name="DEFAULT" styleID="11" fgColor="000000" bgColor="FFFFFF" fontName="" fontStyle="0" fontSize="" />
            <WordsStyle name="INSTRUCTION WORD" styleID="5" fgColor="0000FF" bgColor="FFFFFF" fontName="" fontStyle="1" fontSize="" keywordClass="instre1" />
            <WordsStyle name="TYPE WORD" styleID="16" fgColor="8000FF" bgColor="FFFFFF" fontName="" fontStyle="0" fontSize="" />
            <WordsStyle name="NUMBER" styleID="4" fgColor="FF8000" bgColor="FFFFFF" fontName="" fontStyle="0" fontSize="" />
            <WordsStyle name="STRING" styleID="6" fgColor="808080" bgColor="FFFFFF" fontName="" fontStyle="0" fontSize="" />
            <WordsStyle name="CHARACTER" styleID="7" fgColor="808080" bgColor="FFFFFF" fontName="" fontStyle="0" fontSize="" />
            <WordsStyle name="OPERATOR" styleID="10" fgColor="000080" bgColor="FFFFFF" fontName="" fontStyle="1" fontSize="" />
            <WordsStyle name="VERBATIM" styleID="13" fgColor="000000" bgColor="FFFFFF" fontName="" fontStyle="0" fontSize="" />
            <WordsStyle name="REGEX" styleID="14" fgColor="000000" bgColor="FFFFFF" fontName="" fontStyle="1" fontSize="" />
            <WordsStyle name="COMMENT" styleID="1" fgColor="008000" bgColor="FFFFFF" fontName="" fontStyle="0" fontSize="" />
            <WordsStyle name="COMMENT LINE" styleID="2" fgColor="008000" bgColor="FFFFFF" fontName="" fontStyle="0" fontSize="" />
            <WordsStyle name="COMMENT DOC" styleID="3" fgColor="008080" bgColor="FFFFFF" fontName="" fontStyle="0" fontSize="" />
            <WordsStyle name="COMMENT LINE DOC" styleID="15" fgColor="008080" bgColor="FFFFFF" fontName="" fontStyle="0" fontSize="" />
            <WordsStyle name="COMMENT DOC KEYWORD" styleID="17" fgColor="008080" bgColor="FFFFFF" fontName="" fontStyle="1" fontSize="" />
            <WordsStyle name="COMMENT DOC KEYWORD ERROR" styleID="18" fgColor="008080" bgColor="FFFFFF" fontName="" fontStyle="0" fontSize="" />
        </LexerType>
        <LexerType name="ruby" desc="Ruby" ext="">
            <WordsStyle name="DEFAULT" styleID="0" fgColor="000000" bgColor="FFFFFF" fontName="" fontStyle="0" fontSize="" />
            <WordsStyle name="ERROR" styleID="1" fgColor="000000" bgColor="FFFFFF" fontName="" fontStyle="0" fontSize="" />
            <WordsStyle name="COMMENTLINE" styleID="2" fgColor="008000" bgColor="FFFFFF" fontName="" fontStyle="0" fontSize="" />
            <WordsStyle name="POD" styleID="3" fgColor="004000" bgColor="C0FFC0" fontName="" fontStyle="0" fontSize="" />
            <WordsStyle name="NUMBER" styleID="4" fgColor="FF8000" bgColor="FFFFFF" fontName="" fontStyle="0" fontSize="" />
            <WordsStyle name="INSTRUCTION" styleID="5" fgColor="0000FF" bgColor="FFFFFF" fontName="" fontStyle="1" fontSize="" keywordClass="instre1" />
            <WordsStyle name="STRING" styleID="6" fgColor="808080" bgColor="FFFFFF" fontName="" fontStyle="0" fontSize="" />
            <WordsStyle name="CHARACTER" styleID="7" fgColor="808000" bgColor="FFFFFF" fontName="" fontStyle="0" fontSize="" />
            <WordsStyle name="CLASS NAME" styleID="8" fgColor="0080C0" bgColor="FFFFFF" fontName="" fontStyle="1" fontSize="" />
            <WordsStyle name="DEF NAME" styleID="9" fgColor="8080FF" bgColor="FFFFCC" fontName="" fontStyle="1" fontSize="" />
            <WordsStyle name="OPERATOR" styleID="10" fgColor="000080" bgColor="FFFFFF" fontName="" fontStyle="1" fontSize="" />
            <WordsStyle name="IDENTIFIER" styleID="11" fgColor="000000" bgColor="FFFFFF" fontName="" fontStyle="0" fontSize="" />
            <WordsStyle name="REGEX" styleID="12" fgColor="0080FF" bgColor="FFFFFF" fontName="" fontStyle="0" fontSize="" />
            <WordsStyle name="GLOBAL" styleID="13" fgColor="000080" bgColor="FFFFFF" fontName="" fontStyle="1" fontSize="" />
            <WordsStyle name="SYMBOL" styleID="14" fgColor="000000" bgColor="FFFFFF" fontName="" fontStyle="0" fontSize="" />
            <WordsStyle name="MODULE NAME" styleID="15" fgColor="804000" bgColor="FFFFFF" fontName="" fontStyle="1" fontSize="" />
            <WordsStyle name="INSTANCE VAR" styleID="16" fgColor="000000" bgColor="FFFFFF" fontName="" fontStyle="0" fontSize="" />
            <WordsStyle name="CLASS VAR" styleID="17" fgColor="000000" bgColor="FFFFFF" fontName="" fontStyle="0" fontSize="" />
            <WordsStyle name="BACKTICKS" styleID="18" fgColor="FFFF00" bgColor="A08080" fontName="" fontStyle="0" fontSize="" />
            <WordsStyle name="DATA SECTION" styleID="19" fgColor="600000" bgColor="FFF0D8" fontName="" fontStyle="0" fontSize="" />
            <WordsStyle name="STRING Q" styleID="24" fgColor="808080" bgColor="FFFFFF" fontName="" fontStyle="0" fontSize="" />
        </LexerType>
        <LexerType name="scheme" desc="Scheme" ext="">
            <WordsStyle name="DEFAULT" styleID="0" fgColor="000000" bgColor="FFFFFF" fontName="" fontStyle="0" fontSize="" />
            <WordsStyle name="COMMENTLINE" styleID="1" fgColor="008000" bgColor="FFFFFF" fontName="" fontStyle="0" fontSize="" />
            <WordsStyle name="NUMBER" styleID="2" fgColor="FF8000" bgColor="FFFFFF" fontName="" fontStyle="0" fontSize="" />
            <WordsStyle name="FUNCTION WORD" styleID="3" fgColor="0000FF" bgColor="FFFFFF" fontName="" fontStyle="1" fontSize="" keywordClass="instre1" />
            <WordsStyle name="FUNCTION WORD2" styleID="4" fgColor="0000FF" bgColor="FFFFFF" fontName="" fontStyle="1" fontSize="" keywordClass="instre2" />
            <WordsStyle name="SYMBOL" styleID="5" fgColor="000080" bgColor="FFFFFF" fontName="" fontStyle="1" fontSize="" />
            <WordsStyle name="STRING" styleID="6" fgColor="808080" bgColor="FFFFFF" fontName="" fontStyle="0" fontSize="" />
            <WordsStyle name="IDENTIFIER" styleID="9" fgColor="000000" bgColor="FFFFFF" fontName="" fontStyle="0" fontSize="" />
            <WordsStyle name="OPERATOR" styleID="10" fgColor="0080C0" bgColor="FFFFFF" fontName="" fontStyle="1" fontSize="" keywordClass="type1" />
            <WordsStyle name="SPECIAL" styleID="11" fgColor="800000" bgColor="FFFFFF" fontName="" fontStyle="0" fontSize="" />
            <WordsStyle name="COMMENT" styleID="12" fgColor="808080" bgColor="FFFFFF" fontName="" fontStyle="0" fontSize="" />
        </LexerType>
        <LexerType name="smalltalk" desc="Smalltalk" ext="">
            <WordsStyle name="DEFAULT" styleID="0" fgColor="000000" bgColor="FFFFFF" fontName="" fontStyle="0" fontSize="" />
            <WordsStyle name="STRING" styleID="1" fgColor="808080" bgColor="FFFFFF" fontName="" fontStyle="0" fontSize="" />
            <WordsStyle name="NUMBER" styleID="2" fgColor="FF8000" bgColor="FFFFFF" fontName="" fontStyle="0" fontSize="" />
            <WordsStyle name="COMMENT" styleID="3" fgColor="008000" bgColor="FFFFFF" fontName="" fontStyle="0" fontSize="" />
            <WordsStyle name="SYMBOL" styleID="4" fgColor="408080" bgColor="FFFFFF" fontName="" fontStyle="1" fontSize="" />
            <WordsStyle name="BINARY" styleID="5" fgColor="000080" bgColor="FFFFFF" fontName="" fontStyle="0" fontSize="" />
            <WordsStyle name="BOOL" styleID="6" fgColor="8000FF" bgColor="FFFFFF" fontName="" fontStyle="0" fontSize="" />
            <WordsStyle name="SELF" styleID="7" fgColor="8080FF" bgColor="FFFFCC" fontName="" fontStyle="1" fontSize="" />
            <WordsStyle name="SUPER" styleID="8" fgColor="0080FF" bgColor="ECFFEA" fontName="" fontStyle="1" fontSize="" />
            <WordsStyle name="NIL" styleID="9" fgColor="8080C0" bgColor="FFFFFF" fontName="" fontStyle="0" fontSize="" />
            <WordsStyle name="GLOBAL" styleID="10" fgColor="800000" bgColor="FFFFFF" fontName="" fontStyle="0" fontSize="" />
            <WordsStyle name="RETURN" styleID="11" fgColor="0000FF" bgColor="FFFFFF" fontName="" fontStyle="1" fontSize="" />
            <WordsStyle name="SPECIAL" styleID="12" fgColor="808000" bgColor="FFFFFF" fontName="" fontStyle="0" fontSize="" />
            <WordsStyle name="KWS END" styleID="13" fgColor="0080FF" bgColor="FFFFFF" fontName="" fontStyle="0" fontSize="" />
            <WordsStyle name="ASSIGN" styleID="14" fgColor="FF0000" bgColor="FFFFFF" fontName="" fontStyle="0" fontSize="" />
            <WordsStyle name="CHARACTER" styleID="15" fgColor="808080" bgColor="FFFFFF" fontName="" fontStyle="0" fontSize="" />
            <WordsStyle name="SPECIAL SELECTOR" styleID="16" fgColor="FF80C0" bgColor="FFFFFF" fontName="" fontStyle="0" fontSize="" />
        </LexerType>
        <LexerType name="sql" desc="SQL" ext="">
            <WordsStyle name="KEYWORD" styleID="5" fgColor="0000FF" bgColor="FFFFFF" fontName="" fontStyle="1" fontSize="" keywordClass="instre1" />
            <WordsStyle name="NUMBER" styleID="4" fgColor="FF8000" bgColor="FFFFFF" fontName="" fontStyle="0" fontSize="" />
            <WordsStyle name="STRING" styleID="6" fgColor="808080" bgColor="FFFFFF" fontName="" fontStyle="0" fontSize="" />
            <WordsStyle name="STRING2" styleID="7" fgColor="808080" bgColor="FFFFFF" fontName="" fontStyle="0" fontSize="" />
            <WordsStyle name="OPERATOR" styleID="10" fgColor="000080" bgColor="FFFFFF" fontName="" fontStyle="1" fontSize="" />
            <WordsStyle name="COMMENT" styleID="1" fgColor="008000" bgColor="FFFFFF" fontName="" fontStyle="0" fontSize="" />
            <WordsStyle name="COMMENT LINE" styleID="2" fgColor="008000" bgColor="FFFFFF" fontName="" fontStyle="0" fontSize="" />
        </LexerType>
        <LexerType name="tcl" desc="TCL" ext="">
            <WordsStyle name="DEFAULT" styleID="0" fgColor="000000" bgColor="FFFFFF" fontName="" fontStyle="0" fontSize="" />
            <WordsStyle name="MODIFIER" styleID="10" fgColor="804000" bgColor="FFFFFF" fontName="" fontStyle="0" fontSize="" />
            <WordsStyle name="EXPAND" styleID="11" fgColor="000000" bgColor="FFFFFF" fontName="" fontStyle="0" fontSize="" />
            <WordsStyle name="INSTRUCTION WORD" styleID="12" fgColor="0000FF" bgColor="FFFFFF" fontName="" fontStyle="1" fontSize="" keywordClass="instre1" />
            <WordsStyle name="TYPE WORD" styleID="13" fgColor="8000FF" bgColor="FFFFFF" fontName="" fontStyle="0" fontSize="" keywordClass="type1" />
            <WordsStyle name="NUMBER" styleID="3" fgColor="FF8000" bgColor="FFFFFF" fontName="" fontStyle="0" fontSize="" />
            <WordsStyle name="SUB BRACE" styleID="9" fgColor="808080" bgColor="FFFFFF" fontName="" fontStyle="0" fontSize="" />
            <WordsStyle name="SUBSTITUTION" styleID="8" fgColor="808080" bgColor="FFFFFF" fontName="" fontStyle="0" fontSize="" />
            <WordsStyle name="OPERATOR" styleID="6" fgColor="000080" bgColor="FFFFFF" fontName="" fontStyle="1" fontSize="" />
            <WordsStyle name="IDENTIFIER" styleID="7" fgColor="000000" bgColor="FFFFFF" fontName="" fontStyle="0" fontSize="" />
            <WordsStyle name="WORD IN QUOTE" styleID="4" fgColor="000000" bgColor="FFFFFF" fontName="" fontStyle="1" fontSize="" />
            <WordsStyle name="IN QUOTE" styleID="5" fgColor="000000" bgColor="FFFFFF" fontName="" fontStyle="1" fontSize="" />
            <WordsStyle name="COMMENT" styleID="1" fgColor="008000" bgColor="FFFFFF" fontName="" fontStyle="0" fontSize="" />
            <WordsStyle name="COMMENT LINE" styleID="2" fgColor="008000" bgColor="FFFFFF" fontName="" fontStyle="0" fontSize="" />
            <WordsStyle name="COMMENT BOX" styleID="17" fgColor="008080" bgColor="FFFFFF" fontName="" fontStyle="1" fontSize="" />
            <WordsStyle name="BLOCK COMMENT" styleID="18" fgColor="008080" bgColor="FFFFFF" fontName="" fontStyle="0" fontSize="" />
        </LexerType>
        <LexerType name="tex" desc="TeX" ext="">
            <WordsStyle name="DEFAULT" styleID="0" fgColor="000000" bgColor="FFFFFF" fontName="" fontStyle="0" fontSize="" />
            <WordsStyle name="SPECIAL" styleID="1" fgColor="FF8000" bgColor="FFFFFF" fontName="" fontStyle="1" fontSize="" />
            <WordsStyle name="GROUP" styleID="2" fgColor="8000FF" bgColor="FFFFFF" fontName="" fontStyle="1" fontSize="" />
            <WordsStyle name="SYMBOL" styleID="3" fgColor="800000" bgColor="FFFFFF" fontName="" fontStyle="0" fontSize="" />
            <WordsStyle name="COMMAND" styleID="4" fgColor="0000FF" bgColor="FFFFFF" fontName="" fontStyle="1" fontSize="" />
            <WordsStyle name="TEXT" styleID="5" fgColor="000000" bgColor="FFFFFF" fontName="" fontStyle="0" fontSize="" />
        </LexerType>
        <LexerType name="vb" desc="VB / VBS" ext="">
            <WordsStyle name="DEFAULT" styleID="7" fgColor="000000" bgColor="FFFFFF" fontName="" fontStyle="0" fontSize="" />
            <WordsStyle name="COMMENT" styleID="1" fgColor="008000" bgColor="FFFFFF" fontName="" fontStyle="0" fontSize="" />
            <WordsStyle name="NUMBER" styleID="2" fgColor="FF0000" bgColor="FFFFFF" fontName="" fontStyle="1" fontSize="" />
            <WordsStyle name="WORD" styleID="3" fgColor="0000FF" bgColor="FFFFFF" fontName="" fontStyle="0" fontSize="" keywordClass="instre1" />
            <WordsStyle name="STRING" styleID="4" fgColor="808080" bgColor="FFFFFF" fontName="" fontStyle="0" fontSize="" />
            <WordsStyle name="PREPROCESSOR" styleID="5" fgColor="FF0000" bgColor="FFFFFF" fontName="" fontStyle="0" fontSize="" />
            <WordsStyle name="OPERATOR" styleID="6" fgColor="000000" bgColor="FFFFFF" fontName="" fontStyle="1" fontSize="" />
            <WordsStyle name="DATE" styleID="8" fgColor="00FF00" bgColor="FFFFFF" fontName="" fontStyle="0" fontSize="" />
        </LexerType>
        <LexerType name="verilog" desc="Verilog" ext="">
            <WordsStyle name="DEFAULT" styleID="0" fgColor="000000" bgColor="FFFFFF" fontName="" fontStyle="0" fontSize="" />
            <WordsStyle name="IDENTIFIER" styleID="11" fgColor="000000" bgColor="FFFFFF" fontName="" fontStyle="0" fontSize="" />
            <WordsStyle name="TAGNAME" styleID="2" fgColor="000000" bgColor="FFFFFF" fontName="" fontStyle="0" fontSize="" />
            <WordsStyle name="INSTRUCTION WORD" styleID="5" fgColor="0000FF" bgColor="FFFFFF" fontName="" fontStyle="1" fontSize="" keywordClass="instre1" />
            <WordsStyle name="KEYWORD" styleID="7" fgColor="8000FF" bgColor="FFFFFF" fontName="" fontStyle="0" fontSize="" keywordClass="type1" />
            <WordsStyle name="OPERATOR" styleID="10" fgColor="000080" bgColor="FFFFFF" fontName="" fontStyle="1" fontSize="" />
            <WordsStyle name="NUMBER" styleID="4" fgColor="FF8000" bgColor="FFFFFF" fontName="" fontStyle="0" fontSize="" />
            <WordsStyle name="PREPROCESSOR" styleID="9" fgColor="804000" bgColor="FFFFFF" fontName="" fontStyle="0" fontSize="" />
            <WordsStyle name="STRING" styleID="6" fgColor="808080" bgColor="FFFFFF" fontName="" fontStyle="0" fontSize="" />
            <WordsStyle name="COMMENT" styleID="1" fgColor="008000" bgColor="FFFFFF" fontName="" fontStyle="0" fontSize="" />
            <WordsStyle name="COMMENT LINE" styleID="2" fgColor="008000" bgColor="FFFFFF" fontName="" fontStyle="0" fontSize="" />
            <WordsStyle name="COMMENT LINE BANG" styleID="3" fgColor="008080" bgColor="FFFFFF" fontName="" fontStyle="0" fontSize="" />
            <WordsStyle name="USER" styleID="19" fgColor="000000" bgColor="FFFFFF" fontName="" fontStyle="0" fontSize="" />
        </LexerType>
        <LexerType name="vhdl" desc="VHDL" ext="">
            <WordsStyle name="DEFAULT" styleID="0" fgColor="000000" bgColor="FFFFFF" fontName="" fontStyle="0" fontSize="" />
            <WordsStyle name="COMMENT" styleID="1" fgColor="008000" bgColor="FFFFFF" fontName="" fontStyle="0" fontSize="" />
            <WordsStyle name="COMMENT LIne" styleID="2" fgColor="008000" bgColor="FFFFFF" fontName="" fontStyle="0" fontSize="" />
            <WordsStyle name="NUMBER" styleID="3" fgColor="FF8000" bgColor="FFFFFF" fontName="" fontStyle="0" fontSize="" />
            <WordsStyle name="STRING" styleID="4" fgColor="808080" bgColor="FFFFFF" fontName="" fontStyle="0" fontSize="" />
            <WordsStyle name="OPERATOR" styleID="5" fgColor="000080" bgColor="FFFFFF" fontName="" fontStyle="1" fontSize="" />
            <WordsStyle name="IDENTIFIER" styleID="6" fgColor="000000" bgColor="FFFFFF" fontName="" fontStyle="0" fontSize="" />
            <WordsStyle name="INSTRUCTION" styleID="8" fgColor="0000FF" bgColor="FFFFFF" fontName="" fontStyle="1" fontSize="" keywordClass="instre1" />
            <WordsStyle name="STD OPERATOR" styleID="9" fgColor="0080C0" bgColor="FFFFFF" fontName="" fontStyle="1" fontSize="" keywordClass="instre2" />
            <WordsStyle name="ATTRIBUTE" styleID="10" fgColor="8080FF" bgColor="FFFFCC" fontName="" fontStyle="1" fontSize="" keywordClass="type1" />
            <WordsStyle name="DIRECTIVE" styleID="9" fgColor="808000" bgColor="FFFFFF" fontName="" fontStyle="0" fontSize="" />
            <WordsStyle name="DIRECTIVE OPERAND" styleID="10" fgColor="000080" bgColor="FFFFFF" fontName="" fontStyle="1" fontSize="" />
            <WordsStyle name="STD FUNCTION" styleID="11" fgColor="0080FF" bgColor="FFFFFF" fontName="" fontStyle="1" fontSize="" keywordClass="type2" />
            <WordsStyle name="STD PACKAGE" styleID="12" fgColor="800000" bgColor="FFFFFF" fontName="" fontStyle="0" fontSize="" keywordClass="type3" />
            <WordsStyle name="STD TYPE" styleID="13" fgColor="8000FF" bgColor="FFFFFF" fontName="" fontStyle="0" fontSize="" keywordClass="type4" />
            <WordsStyle name="USER DEFINE" styleID="14" fgColor="B5E71F" bgColor="FFFFFF" fontName="" fontStyle="0" fontSize="" keywordClass="type5" />
        </LexerType>
        <LexerType name="xml" desc="XML" ext="">
            <WordsStyle name="XMLSTART" styleID="12" fgColor="FF0000" bgColor="FFFF00" fontName="" fontStyle="0" fontSize="" />
            <WordsStyle name="XMLEND" styleID="13" fgColor="FF0000" bgColor="FFFF00" fontName="" fontStyle="0" fontSize="" />
            <WordsStyle name="DEFAULT" styleID="0" fgColor="000000" bgColor="FFFFFF" fontName="" fontStyle="1" fontSize="" />
            <WordsStyle name="COMMENT" styleID="9" fgColor="008000" bgColor="FFFFFF" fontName="" fontStyle="0" fontSize="" />
            <WordsStyle name="NUMBER" styleID="5" fgColor="FF0000" bgColor="FFFFFF" fontName="" fontStyle="0" fontSize="" />
            <WordsStyle name="DOUBLESTRING" styleID="6" fgColor="8000FF" bgColor="FFFFFF" fontName="" fontStyle="1" fontSize="" />
            <WordsStyle name="SINGLESTRING" styleID="7" fgColor="8000FF" bgColor="FFFFFF" fontName="" fontStyle="1" fontSize="" />
            <WordsStyle name="TAG" styleID="1" fgColor="0000FF" bgColor="FFFFFF" fontName="" fontStyle="0" fontSize="" />
            <WordsStyle name="TAGEND" styleID="11" fgColor="0000FF" bgColor="FFFFFF" fontName="" fontStyle="0" fontSize="" />
            <WordsStyle name="TAGUNKNOWN" styleID="2" fgColor="0000FF" bgColor="FFFFFF" fontName="" fontStyle="0" fontSize="" />
            <WordsStyle name="ATTRIBUTE" styleID="3" fgColor="FF0000" bgColor="FFFFFF" fontName="" fontStyle="0" fontSize="" />
            <WordsStyle name="ATTRIBUTEUNKNOWN" styleID="4" fgColor="FF0000" bgColor="FFFFFF" fontName="" fontStyle="0" fontSize="" />
            <WordsStyle name="SGMLDEFAULT" styleID="21" fgColor="000000" bgColor="A6CAF0" fontName="" fontStyle="0" fontSize="" />
            <WordsStyle name="CDATA" styleID="17" fgColor="FF8000" bgColor="FFFFFF" fontName="" fontStyle="0" fontSize="" />
        </LexerType>
        <LexerType name="yaml" desc="YAML" ext="">
            <WordsStyle name="DEFAULT" styleID="0" fgColor="000000" bgColor="FFFFFF" fontName="" fontStyle="0" fontSize="" />
            <WordsStyle name="IDENTIFIER" styleID="2" fgColor="000080" bgColor="FFFFFF" fontName="" fontStyle="1" fontSize="" />
            <WordsStyle name="COMMENT" styleID="1" fgColor="008000" bgColor="FFFFFF" fontName="" fontStyle="0" fontSize="" />
            <WordsStyle name="INSTRUCTION WORD" styleID="3" fgColor="0000FF" bgColor="FFFFFF" fontName="" fontStyle="1" fontSize="" keywordClass="instre1" />
            <WordsStyle name="NUMBER" styleID="4" fgColor="FF8040" bgColor="FFFFFF" fontName="" fontStyle="0" fontSize="" />
            <WordsStyle name="REFERENCE" styleID="5" fgColor="804000" bgColor="FFFFFF" fontName="" fontStyle="0" fontSize="" />
            <WordsStyle name="DOCUMENT" styleID="6" fgColor="0000FF" bgColor="FFFFFF" fontName="" fontStyle="0" fontSize="" />
            <WordsStyle name="TEXT" styleID="7" fgColor="808080" bgColor="FFFFFF" fontName="" fontStyle="1" fontSize="" />
            <WordsStyle name="ERROR" styleID="8" fgColor="FF0000" bgColor="FFFFFF" fontName="" fontStyle="0" fontSize="" />
        </LexerType>
        <LexerType name="searchResult" desc="Search result" ext="">
            <WordsStyle name="Default" styleID="0" fgColor="000000" bgColor="FFFFFF" fontName="" fontStyle="0" fontSize="" />
            <WordsStyle name="Search Header" styleID="1" fgColor="000080" bgColor="BBBBFF" fontName="" fontStyle="1" fontSize="" />
            <WordsStyle name="File Header" styleID="2" fgColor="008000" bgColor="D5FFD5" fontName="" fontStyle="1" fontSize="" />
            <WordsStyle name="Line Number" styleID="3" fgColor="000000" bgColor="FFFFFF" fontName="" fontStyle="0" fontSize="" />
            <WordsStyle name="Hit Word" styleID="4" fgColor="FF0000" bgColor="FFFFBF" fontName="" fontStyle="0" fontSize="" />
            <WordsStyle name="Selected Line" styleID="5" fgColor="000080" bgColor="FFFF4F" fontName="" fontStyle="0" fontSize="" />
            <WordsStyle name="Current line background colour" styleID="6" bgColor="E8E8FF" />
        </LexerType>
    </LexerStyles>
    <GlobalStyles>
        <WidgetStyle name="Default Style" fgColor="000000" bgColor="FFFFFF" fontName="Consolas" fontStyle="0" fontSize="10" />
        <WidgetStyle name="Indent guideline style" fgColor="C0C0C0" bgColor="FFFFFF"/>
        <WidgetStyle name="Brace highlight style" fgColor="FF0000" bgColor="FFFFFF" fontSize="12" />
        <WidgetStyle name="Bad brace colour" fgColor="800000" bgColor="FFFFFF" fontName="" fontSize="" />
        <WidgetStyle name="Current line background colour" bgColor="E8E8FF" />
        <WidgetStyle name="Selected text colour" bgColor="C0C0C0" />
        <WidgetStyle name="Caret colour" styleID="2069" fgColor="8000FF" />
        <WidgetStyle name="Edge colour" fgColor="80FFFF" />
        <WidgetStyle name="Line number margin" fgColor="808080" bgColor="333333" fontName="" fontStyle="0" fontSize="" />
        <WidgetStyle name="Fold" fgColor="000000" bgColor="333333" />
        <WidgetStyle name="White space symbol" fgColor="FFB56A" />
    </GlobalStyles>
</styles>
'''
        return s
        
