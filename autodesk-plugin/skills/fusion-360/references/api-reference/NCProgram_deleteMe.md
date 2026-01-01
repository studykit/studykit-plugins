# NCProgram.deleteMe Method

Parent Object: [NCProgram](NCProgram.htm)
Defined in namespace "adsk::cam" and the header file is <Cam/NCProgram/NCProgram.h>

## Description

Deletes the operation from the document. In case of a setup or folder, all containing child operations will be deleted as well. Note: Child classes may overwrite this function and throw an exception if the object cannot be deleted.

## Syntax

* [Python](#Python)
* [C++](#C++)

"nCProgram\_var" is a variable referencing a [NCProgram](NCProgram.htm) object.```` ``` returnValue = nCProgram_var.deleteMe() ``` ```` |

"nCProgram\_var" is a variable referencing a [NCProgram](NCProgram.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| boolean | Returns true if the delete was successful. |

## Version

Introduced in version May 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |