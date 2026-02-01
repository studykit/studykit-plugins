# RenderEnvironments.itemByName Method

Parent Object: [RenderEnvironments](RenderEnvironments.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Render/RenderEnvironments.h>

## Description

Returns the specified render environment using the name as seen in the user interface.

## Syntax

* [Python](#Python)
* [C++](#C++)

"renderEnvironments\_var" is a variable referencing a [RenderEnvironments](RenderEnvironments.htm) object.```` ``` returnValue = renderEnvironments_var.itemByName(name) ``` ```` |

"renderEnvironments\_var" is a variable referencing a [RenderEnvironments](RenderEnvironments.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [RenderEnvironment](RenderEnvironment.htm) | Returns the specified render environment or null if there's no match on the name. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| name | string | The name of the render environment to return. |

## Version

Introduced in version May 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |