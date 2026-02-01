# EmbossFeatureInput.profiles Property![](../images/TestTubeLarge.png)

Parent Object: [EmbossFeatureInput](EmbossFeatureInput.htm)

![Preview](../images/TestTubeSmall.png)This functionality is provided as a preview
of intended future API capabilities. You are encouraged to use it and report any problems or suggestions using the
[Fusion API and Scripts](https://forums.autodesk.com/t5/fusion-360-api-and-scripts/bd-p/22) forum.

Because this is a preview of future functionality, there is the possibility that it will change, which will possibly
break any existing programs that use this functionality. Because of that, you should never deliver any programs that use
any preview capabilities. For a distributed program, you should wait until it has moved from preview to released state.

Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/EmbossFeatureInput.h>

## Description

Gets and sets an array of Profile objects that define the shape of the emboss. The profile argument can be Profile and SketchText objects. When multiple objects are used, all profiles and sketch texts must be co-planar.

## Syntax

* [Python](#Python)
* [C++](#C++)

"embossFeatureInput\_var" is a variable referencing an EmbossFeatureInput object. |

"embossFeatureInput\_var" is a variable referencing an EmbossFeatureInput object. ```` ``` #include <Fusion/Features/EmbossFeatureInput.h>  // Get the value of the property. std::vector<Ptr<Base>> propertyValue = embossFeatureInput_var->profiles();  // Set the value of the property, where value_var is a Base. bool returnValue = embossFeatureInput_var->profiles(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is an array of type [Base](Base.htm).

## Version

Introduced in version September 2025

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |