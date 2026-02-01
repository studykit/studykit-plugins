# IntegerGraphNodeProperty.isValid Property![](../images/TestTubeLarge.png)

Parent Object: [IntegerGraphNodeProperty](IntegerGraphNodeProperty.htm)

![Preview](../images/TestTubeSmall.png)This functionality is provided as a preview
of intended future API capabilities. You are encouraged to use it and report any problems or suggestions using the
[Fusion API and Scripts](https://forums.autodesk.com/t5/fusion-360-api-and-scripts/bd-p/22) forum.

Because this is a preview of future functionality, there is the possibility that it will change, which will possibly
break any existing programs that use this functionality. Because of that, you should never deliver any programs that use
any preview capabilities. For a distributed program, you should wait until it has moved from preview to released state.

Defined in namespace "adsk::volume" and the header file is <Volume/Volumetric/IntegerGraphNodeProperty.h>

## Description

Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

## Syntax

* [Python](#Python)
* [C++](#C++)

"integerGraphNodeProperty\_var" is a variable referencing an IntegerGraphNodeProperty object. |

"integerGraphNodeProperty\_var" is a variable referencing an IntegerGraphNodeProperty object. ```` ``` #include <Volume/Volumetric/IntegerGraphNodeProperty.h>  // Get the value of the property. boolean propertyValue = integerGraphNodeProperty_var->isValid(); ``` ```` |

## Property Value

This is a read only property whose value is a boolean.

## Version

Introduced in version May 2025

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |