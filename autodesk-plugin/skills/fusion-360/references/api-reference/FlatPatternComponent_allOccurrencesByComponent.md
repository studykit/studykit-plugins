# FlatPatternComponent.allOccurrencesByComponent Method

Parent Object: [FlatPatternComponent](FlatPatternComponent.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/SheetMetal/FlatPatternComponent.h>

## Description

Returns all occurrences, at any level of the assembly, that reference the specified component. The returned list is read-only.

## Syntax

* [Python](#Python)
* [C++](#C++)

"flatPatternComponent\_var" is a variable referencing a [FlatPatternComponent](FlatPatternComponent.htm) object.```` ``` returnValue = flatPatternComponent_var.allOccurrencesByComponent(component) ``` ```` |

"flatPatternComponent\_var" is a variable referencing a [FlatPatternComponent](FlatPatternComponent.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [OccurrenceList](OccurrenceList.htm) | The occurrences referenced by the specified component. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| component | [Component](Component.htm) | The component that is being referenced by the occurrences that will be returned. |

## Version

Introduced in version October 2022

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |