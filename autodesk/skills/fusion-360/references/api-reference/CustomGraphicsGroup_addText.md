# CustomGraphicsGroup.addText Method

Parent Object: [CustomGraphicsGroup](CustomGraphicsGroup.htm)
Defined in namespace "adsk::fusion" and the header file is <Fusion/Graphics/CustomGraphicsGroup.h>

## Description

Adds a new CustomGraphicsText entity to this group. This will be displayed as a single line of text. It is placed so that the upper-left corner is at the point defined and the text will be parallel to the X-Y plane of the world coordinate system and in the X direction. To change it's position relative to the input point you can change the horizontal and vertical justification on the returned CustomGrahicsText object. You can also reorient the text by changing the transform of the returned CustomGraphicsText object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"customGraphicsGroup\_var" is a variable referencing a [CustomGraphicsGroup](CustomGraphicsGroup.htm) object.```` ``` returnValue = customGraphicsGroup_var.addText(formattedText, font, size, transform) ``` ```` |

"customGraphicsGroup\_var" is a variable referencing a [CustomGraphicsGroup](CustomGraphicsGroup.htm) object. |

## Return Value

|  |  |
| --- | --- |
| Type | Description |
| [CustomGraphicsText](CustomGraphicsText.htm) | Returns the newly created CustomGraphicsText object or null in the case of failure. |

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| formattedText | string | The text string to be displayed. Overall formatting can be defined using properties on the returned CustomGraphicsText object. Formatting overrides can be defined within the string using formatting codes. |
| font | string | The name of the font to use when displaying the text. |
| size | double | The size of the text in centimeters. |
| transform | [Matrix3D](Matrix3D.htm) | Transformation matrix that specifies the position and orientation of the text in model space. The origin of the text is the upper-left corner. |

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Custom Graphics Sample](CustomGraphicsSample_Sample.htm) | A sample demonstrating how to create custom graphics entities.  To use the sample, create a new Python or C++ script and copy and paste this code, replacing the default code. You also need to unpack this zip file which contains a [resource folder](../ExtraFiles/GraphicsSampleResources.zip) into the same folder where the source code file (.py or .cpp) is. |

## Version

Introduced in version April 2019

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |