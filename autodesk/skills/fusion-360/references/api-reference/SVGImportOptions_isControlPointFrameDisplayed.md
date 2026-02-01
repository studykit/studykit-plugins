# SVGImportOptions.isControlPointFrameDisplayed Property

Parent Object: [SVGImportOptions](SVGImportOptions.htm)
Defined in namespace "adsk::core" and the header file is <Core/Application/SVGImportOptions.h>

## Description

Gets and sets if any spline curves in the SVG should be drawn with their control point frames. This property defaults to false in a newly created SVGImportOptions object.

## Syntax

* [Python](#Python)
* [C++](#C++)

"sVGImportOptions\_var" is a variable referencing a SVGImportOptions object. |

"sVGImportOptions\_var" is a variable referencing a SVGImportOptions object. ```` ``` #include <Core/Application/SVGImportOptions.h>  // Get the value of the property. boolean propertyValue = sVGImportOptions_var->isControlPointFrameDisplayed();  // Set the value of the property, where value_var is a boolean. bool returnValue = sVGImportOptions_var->isControlPointFrameDisplayed(value_var); ``` ```` |

## Property Value

This is a read/write property whose value is a boolean.

## Version

Introduced in version October 2022

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |