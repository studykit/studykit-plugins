# SketchText Object

Derived from: [SketchEntity](SketchEntity.htm) Object

Defined in namespace "adsk::fusion" and the header file is <Fusion/Sketch/SketchText.h>

## Description

Text in a sketch.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [asCurves](SketchText_asCurves.htm) | Returns the underlying curves that define the outline of the text. Calling this does not affect the SketchText and does not create any new sketch geometry but returns the geometrical definition of the sketch outline. |
| [classType](SketchText_classType.htm) | Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType(). |
| [createForAssemblyContext](SketchText_createForAssemblyContext.htm) | Creates a proxy object for the SketchText object that represents the SketchText object in the context of an assembly. The context is defined by the input occurrence. |
| [deleteMe](SketchText_deleteMe.htm) | Deletes the entity from the sketch. |
| [explode](SketchText_explode.htm) | Explodes the SketchText into a set of curves. The original SketchText is deleted as a result of calling this. |
| [redefineAsAlongPath](SketchText_redefineAsAlongPath.htm) | Sets this SketchTextInput to define text that follows along a specified path. |
| [redefineAsFitOnPath](SketchText_redefineAsFitOnPath.htm) | Sets this SketchTextInput to define text that fits along a specified path. Fitting on a path will space the characters so the text fits along the entire length of the path entity. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [angle](SketchText_angle.htm) | \*\*RETIRED\*\* Gets and sets the angle of the text relative to the x-axis of the x-y plane of the sketch. |
| [assemblyContext](SketchText_assemblyContext.htm) | Returns the assembly occurrence (i.e. the occurrence) of this object in an assembly. This is only valid in the case where this is acting as a proxy in an assembly. Returns null in the case where the object is not in the context of an assembly but is already the native object. |
| [attributes](SketchText_attributes.htm) | Returns the collection of attributes associated with this face. |
| [boundaryLines](SketchText_boundaryLines.htm) | \*\*RETIRED\*\* Returns the four sketch lines that define the boundary of the sketch text. By adding constraints to these lines you can associatively control the size, position and angle of the sketch text. |
| [boundingBox](SketchText_boundingBox.htm) | Returns the bounding box of the entity in sketch space. |
| [definition](SketchText_definition.htm) | Gets the definition that is currently used to specify how the sketch text is defined. |
| [entityToken](SketchText_entityToken.htm) | Returns a token for the SketchEntity object. This can be saved and used at a later time with the Design.findEntityByToken method to get back the same sketch entity. |
| [fontName](SketchText_fontName.htm) | Gets and sets the name of the font to use. |
| [geometricConstraints](SketchText_geometricConstraints.htm) | Returns the sketch constraints that are attached to this curve. |
| [height](SketchText_height.htm) | Gets and sets the height of the text in centimeters. |
| [is2D](SketchText_is2D.htm) | Indicates if this curve lies entirely on the sketch x-y plane. |
| [isDeletable](SketchText_isDeletable.htm) | Indicates if this sketch entity can be deleted. There are cases, especially with sketch points where another entity is dependent on an entity so deleting it is not allowed. For example, you can't delete the center point of circle by itself but deleting the circle will delete the point. The same is true for the end points of a line. |
| [isFixed](SketchText_isFixed.htm) | Indicates if this geometry is "fixed". |
| [isFullyConstrained](SketchText_isFullyConstrained.htm) | Indicates if this sketch entity is fully constrained. |
| [isHorizontalFlip](SketchText_isHorizontalFlip.htm) | Gets and sets if the text is flipped horizontally. |
| [isLinked](SketchText_isLinked.htm) | Indicates if this sketch entity was created by a projection, inclusion, or driven by an API script. If this returns true, then the entity is presented to the user as not editable and with a 'break link' command available. |
| [isReference](SketchText_isReference.htm) | Indicates if this geometry is a reference. Changing this property from true to false removes the reference. This property can not be set to true if it is already false. |
| [isValid](SketchText_isValid.htm) | Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference. |
| [isVerticalFlip](SketchText_isVerticalFlip.htm) | Gets and sets if the text is flipped vertically. |
| [isVisible](SketchText_isVisible.htm) | When a sketch is created, geometry is sometimes automatically added to the sketch. For example a sketch point that references the origin point is always included and if a face was selected to create the sketch on, geometry from the face is also included. This automatically created geometry behaves in a special way in that it is invisible but is available for selection and it also participates in profile calculations. It's not possible to make them visible but they can be deleted and they can be used for any other standard sketch operation. |
| [nativeObject](SketchText_nativeObject.htm) | The NativeObject is the object outside the context of an assembly and in the context of it's parent component. Returns null in the case where this object is not in the context of an assembly but is already the native object. |
| [objectType](SketchText_objectType.htm) | This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.   It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType(): |
| [parentSketch](SketchText_parentSketch.htm) | Returns the parent sketch. |
| [position](SketchText_position.htm) | \*\*RETIRED\*\* Gets and sets the position of the text on the x-y plane of the sketch. The text must lie on the x-y plane so the Z component of the point is ignored and always treated as zero. |
| [referencedEntity](SketchText_referencedEntity.htm) | Returns the referenced entity in the case where IsReference is true. However, this property can also return null when IsReference is true in the case where the reference is not parametric. |
| [sketchDimensions](SketchText_sketchDimensions.htm) | Returns the sketch dimensions that are attached to this curve. |
| [text](SketchText_text.htm) | Gets and sets the text. This is a simple string and ignores any formatting defined within the text. |
| [textStyle](SketchText_textStyle.htm) | Gets and sets the text style to apply to the entire text. This is a bitwise enum so styles can be combined to apply multiple styles. For example you can apply bold and underline. |

## Accessed From

[AlongPathTextDefinition.parentSketchText](AlongPathTextDefinition_parentSketchText.htm), [FitOnPathTextDefintion.parentSketchText](FitOnPathTextDefintion_parentSketchText.htm), [MultiLineTextDefinition.parentSketchText](MultiLineTextDefinition_parentSketchText.htm), [SketchText.createForAssemblyContext](SketchText_createForAssemblyContext.htm), [SketchText.nativeObject](SketchText_nativeObject.htm), [SketchTextDefinition.parentSketchText](SketchTextDefinition_parentSketchText.htm), [SketchTexts.add](SketchTexts_add.htm), [SketchTexts.item](SketchTexts_item.htm)

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Sketch Text API Sample](SketchTextSample_Sample.htm) | Demonstrates creating sketch text by creating both mult-line text and text along a curve. |

## Version

Introduced in version March 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |