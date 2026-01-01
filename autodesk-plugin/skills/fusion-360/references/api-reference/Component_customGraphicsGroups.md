# Component.customGraphicsGroups Property

Parent Object: [Component](Component.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Components/Component.h>

## Description

Returns the customGraphicsGroups object in this component.

## Syntax

* [Python](#Python)
* [C++](#C++)

"component\_var" is a variable referencing a Component object. |

"component\_var" is a variable referencing a Component object. ```` ``` #include <Fusion/Components/Component.h>  // Get the value of the property. Ptr<CustomGraphicsGroups> propertyValue = component_var->customGraphicsGroups(); ``` ```` |

## Property Value

This is a read only property whose value is a [CustomGraphicsGroups](CustomGraphicsGroups.htm).

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