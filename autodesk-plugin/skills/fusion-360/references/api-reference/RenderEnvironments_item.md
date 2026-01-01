# RenderEnvironments.item Method

Parent Object: [RenderEnvironments](RenderEnvironments.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Render/RenderEnvironments.h>

## Description

Method that returns the specified render environment using an index into the collection.

## Syntax

* [Python](#Python)
* [C++](#C++)

"renderEnvironments\_var" is a variable referencing a [RenderEnvironments](RenderEnvironments.htm) object.```` ``` returnValue = renderEnvironments_var.item(index) ``` ```` |

"renderEnvironments\_var" is a variable referencing a [RenderEnvironments](RenderEnvironments.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [RenderEnvironment](RenderEnvironment.htm) | Returns the specified render environment or null if an invalid index was specified. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| index | integer | The index of the item within the collection. The first item has an index of 0. |

## Version

Introduced in version May 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |