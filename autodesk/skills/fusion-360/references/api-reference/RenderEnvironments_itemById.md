# RenderEnvironments.itemById Method

Parent Object: [RenderEnvironments](RenderEnvironments.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Render/RenderEnvironments.h>

## Description

Returns the render environment with the specified ID.

## Syntax

* [Python](#Python)
* [C++](#C++)

"renderEnvironments\_var" is a variable referencing a [RenderEnvironments](RenderEnvironments.htm) object.```` ``` returnValue = renderEnvironments_var.itemById(id) ``` ```` |

"renderEnvironments\_var" is a variable referencing a [RenderEnvironments](RenderEnvironments.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [RenderEnvironment](RenderEnvironment.htm) | Returns the specified render environment or null if the ID does not match a render environment. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| id | string | The ID of the render environment to return. |

## Version

Introduced in version May 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |