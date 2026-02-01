# CustomFeatureDefinition.iconFolder Property![](../images/TestTubeLarge.png)

Parent Object: [CustomFeatureDefinition](CustomFeatureDefinition.htm)

![Preview](../images/TestTubeSmall.png)This functionality is provided as a preview
of intended future API capabilities. You are encouraged to use it and report any problems or suggestions using the
[Fusion API and Scripts](https://forums.autodesk.com/t5/fusion-360-api-and-scripts/bd-p/22) forum.

Because this is a preview of future functionality, there is the possibility that it will change, which will possibly
break any existing programs that use this functionality. Because of that, you should never deliver any programs that use
any preview capabilities. For a distributed program, you should wait until it has moved from preview to released state.

Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/CustomFeatureDefinition.h>

## Description

Gets and sets the folder that contains the images that are used for the icon in the timeline for this custom feature. The folder should contain the image files named 16x16.png and 32x32.png which should be images that are 16 and 32 pixels square.

## Syntax

* [Python](#Python)
* [C++](#C++)

"customFeatureDefinition\_var" is a variable referencing a CustomFeatureDefinition object. |

"customFeatureDefinition\_var" is a variable referencing a CustomFeatureDefinition object. ```` ``` #include <Fusion/Features/CustomFeatureDefinition.h>  // Get the value of the property. string propertyValue = customFeatureDefinition_var->iconFolder();  // Set the value of the property, where value_var is a string. bool returnValue = customFeatureDefinition_var->iconFolder(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a string.

## Version

Introduced in version January 2021

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |