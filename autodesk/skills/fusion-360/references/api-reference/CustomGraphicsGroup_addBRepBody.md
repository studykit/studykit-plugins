# CustomGraphicsGroup.addBRepBody Method

Parent Object: [CustomGraphicsGroup](CustomGraphicsGroup.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Graphics/CustomGraphicsGroup.h>

## Description

Adds a new CustomGraphicsBRepBody object to this group. This displays a real or transient BRepBody object as custom graphics. No relationship exists back to the original input body so if it is changed, the custom graphics will not change.

## Syntax

* [Python](#Python)
* [C++](#C++)

"customGraphicsGroup\_var" is a variable referencing a [CustomGraphicsGroup](CustomGraphicsGroup.htm) object.```` ``` returnValue = customGraphicsGroup_var.addBRepBody(body) ``` ```` |

"customGraphicsGroup\_var" is a variable referencing a [CustomGraphicsGroup](CustomGraphicsGroup.htm) object.  ```` ``` #include <Fusion/Graphics/CustomGraphicsGroup.h>  returnValue = customGraphicsGroup_var->addBRepBody(body); ``` ```` |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [CustomGraphicsBRepBody](CustomGraphicsBRepBody.htm) | Returns the newly created CustomGraphicsBRepBody object or null in the case of failure. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| body | [BRepBody](BRepBody.htm) | The real or transient BRepBody object to draw using custom graphics. |

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Custom Graphics Sample](CustomGraphicsSample_Sample.htm) | A sample demonstrating how to create custom graphics entities.  To use the sample, create a new Python or C++ script and copy and paste this code, replacing the default code. You also need to unpack this zip file which contains a [resource folder](../ExtraFiles/GraphicsSampleResources.zip) into the same folder where the source code file (.py or .cpp) is. |

## Version

Introduced in version September 2017

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |