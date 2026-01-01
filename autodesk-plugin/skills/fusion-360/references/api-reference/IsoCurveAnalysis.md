# IsoCurveAnalysis Object

Derived from: [Analysis](Analysis.htm) Object

Defined in namespace "adsk::fusion" and the header file is <Fusion/Fusion/IsoCurveAnalysis.h>

## Description

Represents any existing Iso Curve Analysis that exist in the design.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [classType](IsoCurveAnalysis_classType.htm) | Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType(). |
| [deleteMe](IsoCurveAnalysis_deleteMe.htm) | A method that deletes this Analysis. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [attributes](IsoCurveAnalysis_attributes.htm) | A property that returns the collection of attributes associated with this Analysis. |
| [entityToken](IsoCurveAnalysis_entityToken.htm) | Returns a token for the Analysis object. The token can be saved and used later with the Design.findEntityByToken method to get back the same Analysis. |
| [isLightBulbOn](IsoCurveAnalysis_isLightBulbOn.htm) | A property that gets and sets if the display is enabled for this Analysis object. If false, this analysis will be hidden. If true and the IsLightBulbOn property of the Analyses object is True the Analysis will be visible. |
| [isValid](IsoCurveAnalysis_isValid.htm) | Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference. |
| [isVisible](IsoCurveAnalysis_isVisible.htm) | Gets if this Analysis is currently visible in the graphics window. The visibility is controlled by a combination of the isLightBulbOn properties of the Analyses collection object and the Analysis object. If both are true, the Analysis will be visible. |
| [name](IsoCurveAnalysis_name.htm) | A property that gets and sets the name of the analysis. If you use a name that is not unique, Fusion will automatically append a number to the name to make it unique. |
| [objectType](IsoCurveAnalysis_objectType.htm) | This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.   It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType(): |

## Accessed From

[IsoCurveAnalyses.item](IsoCurveAnalyses_item.htm), [IsoCurveAnalyses.itemByName](IsoCurveAnalyses_itemByName.htm)

## Version

Introduced in version January 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |