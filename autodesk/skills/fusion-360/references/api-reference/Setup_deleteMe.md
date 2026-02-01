# Setup.deleteMe Method

Parent Object: [Setup](Setup.htm)
Defined in namespace "adsk::cam" and the header file is <Cam/CAM/Setup.h>

## Description

Deletes the operation from the document. In case of a setup or folder, all containing child operations will be deleted as well. Note: Child classes may overwrite this function and throw an exception if the object cannot be deleted.

## Syntax

* [Python](#Python)
* [C++](#C++)

"setup\_var" is a variable referencing a [Setup](Setup.htm) object.```` ``` returnValue = setup_var.deleteMe() ``` ```` |

"setup\_var" is a variable referencing a [Setup](Setup.htm) object. |

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