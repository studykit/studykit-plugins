# Components.itemById Method

Parent Object: [Components](Components.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Components/Components.h>

## Description

Returns the Component that has the specified ID.

## Syntax

* [Python](#Python)
* [C++](#C++)

"components\_var" is a variable referencing a [Components](Components.htm) object.```` ``` returnValue = components_var.itemById(id) ``` ```` |

"components\_var" is a variable referencing a [Components](Components.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [Component](Component.htm) | Returns the specified Component or null in the case where there isn't a Component with the specified ID in this Design. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| id | string | The ID of the Component to get. This is the same id used by PIM (Product Information Model). |

## Version

Introduced in version December 2020

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |