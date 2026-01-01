# OpenHemFeatureDefinition Object ![Preview](../images/TestTubeLarge.png)

Derived from: [HemFeatureDefinition](HemFeatureDefinition.htm) Object

Defined in namespace "adsk::fusion" and the header file is <Fusion/SheetMetal/OpenHemFeatureDefinition.h>

![Preview](../images/TestTubeSmall.png)This functionality is provided as a preview
of intended future API capabilities. You are encouraged to use it and report any problems or suggestions using the
[Fusion API and Scripts](https://forums.autodesk.com/t5/fusion-360-api-and-scripts/bd-p/22) forum.

Because this is a preview of future functionality, there is the possibility that it will change, which will possibly
break any existing programs that use this functionality. Because of that, you should never deliver any programs that use
any preview capabilities. For a distributed program, you should wait until it has moved from preview to released state.

## Description

The definition for an open hem.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [classType](OpenHemFeatureDefinition_classType.htm) | Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType(). |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [bendPositionType](OpenHemFeatureDefinition_bendPositionType.htm) | Gets the bend position type for a hem. |
| [gap](OpenHemFeatureDefinition_gap.htm) | Gets the gap for an open hem. |
| [hemEdge](OpenHemFeatureDefinition_hemEdge.htm) | Gets and sets the input edge for a hem |
| [isFlipped](OpenHemFeatureDefinition_isFlipped.htm) | Gets the flip direction for an open hem. |
| [isValid](OpenHemFeatureDefinition_isValid.htm) | Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference. |
| [length](OpenHemFeatureDefinition_length.htm) | Gets the length for an open hem. |
| [objectType](OpenHemFeatureDefinition_objectType.htm) | This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object. |

## Version

Introduced in version September 2025

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |