# IsoCurveAnalyses Object

Derived from: [Base](Base.htm) Object

Defined in namespace "adsk::fusion" and the header file is <Fusion/Fusion/IsoCurveAnalyses.h>

## Description

Provides access to any Iso Curve analyses results in the design.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [classType](IsoCurveAnalyses_classType.htm) | Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType(). |
| [item](IsoCurveAnalyses_item.htm) | A method that returns the specified IsoCurveAnalysis object using an index into the collection. |
| [itemByName](IsoCurveAnalyses_itemByName.htm) | A method that returns the specified IsoCurveAnalysis object using the name of the analysis as displayed in the browser. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [count](IsoCurveAnalyses_count.htm) | Returns the number of CurvatureCombAnalysis objects in the collection. |
| [isValid](IsoCurveAnalyses_isValid.htm) | Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference. |
| [objectType](IsoCurveAnalyses_objectType.htm) | This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object. |

## Accessed From

[Analyses.isoCurveAnalyses](Analyses_isoCurveAnalyses.htm)

## Version

Introduced in version January 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |