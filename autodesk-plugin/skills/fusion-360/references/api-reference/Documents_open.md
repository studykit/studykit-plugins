# Documents.open Method

Parent Object: [Documents](Documents.htm)
Defined in namespace "adsk::core" and the header file is <Core/Application/Documents.h>

## Description

Opens an item that has previously been saved.

## Syntax

* [Python](#Python)
* [C++](#C++)

"documents\_var" is a variable referencing a [Documents](Documents.htm) object.```` ``` # Uses no optional arguments. ``` ```` |

"documents\_var" is a variable referencing a [Documents](Documents.htm) object.  ```` ``` #include <Core/Application/Documents.h>  // Uses no optional arguments. returnValue = documents_var->open(dataFile);  // Uses optional arguments. returnValue = documents_var->open(dataFile, visible); ``` ```` |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [Document](Document.htm) | Returns the open document or null if the open failed. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| dataFile | [DataFile](DataFile.htm) | The item to open. |
| visible | boolean | Specifies if the document should be opened visibly or not.   This is an optional argument whose default value is True. |

## Version

Introduced in version March 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |