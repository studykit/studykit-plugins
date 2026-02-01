# RolledHemFeatureDefinition.hemEdge Property![](../images/TestTubeLarge.png)

Parent Object: [RolledHemFeatureDefinition](RolledHemFeatureDefinition.htm)

![Preview](../images/TestTubeSmall.png)This functionality is provided as a preview
of intended future API capabilities. You are encouraged to use it and report any problems or suggestions using the
[Fusion API and Scripts](https://forums.autodesk.com/t5/fusion-360-api-and-scripts/bd-p/22) forum.

Because this is a preview of future functionality, there is the possibility that it will change, which will possibly
break any existing programs that use this functionality. Because of that, you should never deliver any programs that use
any preview capabilities. For a distributed program, you should wait until it has moved from preview to released state.

Defined in namespace "adsk::fusion" and the header file is <Fusion/SheetMetal/RolledHemFeatureDefinition.h>

## Description

Gets and sets the input edge for a hem

## Syntax

* [Python](#Python)
* [C++](#C++)

"rolledHemFeatureDefinition\_var" is a variable referencing a RolledHemFeatureDefinition object. |

"rolledHemFeatureDefinition\_var" is a variable referencing a RolledHemFeatureDefinition object. ```` ``` #include <Fusion/SheetMetal/RolledHemFeatureDefinition.h>  // Get the value of the property. Ptr<BRepEdge> propertyValue = rolledHemFeatureDefinition_var->hemEdge();  // Set the value of the property, where value_var is a BRepEdge. bool returnValue = rolledHemFeatureDefinition_var->hemEdge(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a [BRepEdge](BRepEdge.htm).

## Version

Introduced in version September 2025

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |