# SectionAnalysis Object

Derived from: [Analysis](Analysis.htm) Object

Defined in namespace "adsk::fusion" and the header file is <Fusion/Fusion/SectionAnalysis.h>

## Description

Represents any existing Section Analysis that exist in the design.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [classType](SectionAnalysis_classType.htm) | Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType(). |
| [deleteMe](SectionAnalysis_deleteMe.htm) | A method that deletes this Analysis. |
| [flip](SectionAnalysis_flip.htm) | A property that flips which side of the part is cut away by the section. This is a convenience method that results in flipping the Z axis of the transform while maintaining a valid rectangular coordinate system. You can directly manipulate the transform matrix to have the same effect. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [attributes](SectionAnalysis_attributes.htm) | A property that returns the collection of attributes associated with this Analysis. |
| [cutPlane](SectionAnalysis_cutPlane.htm) | A property that gets and sets the planar entity used to define the cut plane and can be either a planar BRepFace or a ConstructionPlane object. |
| [entityToken](SectionAnalysis_entityToken.htm) | Returns a token for the Analysis object. The token can be saved and used later with the Design.findEntityByToken method to get back the same Analysis. |
| [initialPosition](SectionAnalysis_initialPosition.htm) | Returns the matrix that describes the initial position and orientation of the specified cut plane entity. Any additional offsets or rotations are defined by a transformation matrix that is applied to this initial position. That matrix can be obtained and set using the transform property. |
| [isHatchShown](SectionAnalysis_isHatchShown.htm) | A property that gets and sets if a hatch pattern should be shown on the section. |
| [isLightBulbOn](SectionAnalysis_isLightBulbOn.htm) | A property that gets and sets if the display is enabled for this Analysis object. If false, this analysis will be hidden. If true and the IsLightBulbOn property of the Analyses object is True the Analysis will be visible. |
| [isValid](SectionAnalysis_isValid.htm) | Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference. |
| [isVisible](SectionAnalysis_isVisible.htm) | Gets if this Analysis is currently visible in the graphics window. The visibility is controlled by a combination of the isLightBulbOn properties of the Analyses collection object and the Analysis object. If both are true, the Analysis will be visible. |
| [name](SectionAnalysis_name.htm) | A property that gets and sets the name of the analysis. If you use a name that is not unique, Fusion will automatically append a number to the name to make it unique. |
| [objectType](SectionAnalysis_objectType.htm) | This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.   It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType(): |
| [sectionColor](SectionAnalysis_sectionColor.htm) | A property that gets and sets the color of the section. A value of null indicates the component color should be used. The opacity value of the color is ignored. |
| [transform](SectionAnalysis_transform.htm) | The initial position of the section plane is defined by the specified cut plane entity. Any offsets or rotations are defined by a transformation matrix that is applied to the initial position. This property allows you to get and set the transformation matrix. |

## Accessed From

[SectionAnalyses.add](SectionAnalyses_add.htm), [SectionAnalyses.item](SectionAnalyses_item.htm), [SectionAnalyses.itemByName](SectionAnalyses_itemByName.htm)

## Version

Introduced in version January 2023

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |