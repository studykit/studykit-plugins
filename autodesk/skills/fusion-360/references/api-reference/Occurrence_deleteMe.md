# Occurrence.deleteMe Method

Parent Object: [Occurrence](Occurrence.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Components/Occurrence.h>

## Description

Deletes the occurrence from the design. If this is the last occurrence referencing a specific Component, the component is also deleted.

## Syntax

* [Python](#Python)
* [C++](#C++)

"occurrence\_var" is a variable referencing an [Occurrence](Occurrence.htm) object.```` ``` returnValue = occurrence_var.deleteMe() ``` ```` |

"occurrence\_var" is a variable referencing an [Occurrence](Occurrence.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| boolean | Returns true if the delete was successful. |

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Delete Empty Components](DeleteEmptyComponents_Sample.htm) | Deletes empty components from the active design. |

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |