# Component.allOccurrencesByComponent Method

Parent Object: [Component](Component.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Components/Component.h>

## Description

Returns all occurrences, at any level of the assembly, that reference the specified component. The returned list is read-only.

## Syntax

* [Python](#Python)
* [C++](#C++)

"component\_var" is a variable referencing a [Component](Component.htm) object.```` ``` returnValue = component_var.allOccurrencesByComponent(component) ``` ```` |

"component\_var" is a variable referencing a [Component](Component.htm) object. |

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