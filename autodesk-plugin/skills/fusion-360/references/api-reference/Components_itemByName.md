# Components.itemByName Method

Parent Object: [Components](Components.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Components/Components.h>

## Description

Function that returns the specified component by name.

## Syntax

* [Python](#Python)
* [C++](#C++)

"components\_var" is a variable referencing a [Components](Components.htm) object.```` ``` returnValue = components_var.itemByName(name) ``` ```` |

"components\_var" is a variable referencing a [Components](Components.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [Component](Component.htm) | Returns the specified component or null if the name is not found. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| name | string | The name of the component within the collection to return. |

## Version

Introduced in version January 2016

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |