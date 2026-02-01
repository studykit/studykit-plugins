# GeometricConstraints Object

Derived from: [Base](Base.htm) Object

Defined in namespace "adsk::fusion" and the header file is <Fusion/Sketch/GeometricConstraints.h>

## Description

A collection of all of the geometric constraints in a sketch. This object also supports the methods to create new geometric constraints.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [addCircularPattern](GeometricConstraints_addCircularPattern.htm) | Creates a new circular pattern in the sketch. |
| [addCoincident](GeometricConstraints_addCoincident.htm) | Creates a new coincident constraint between two entities. The first argument is a sketch point. The second argument is a sketch curve or point. |
| [addCoincidentToSurface](GeometricConstraints_addCoincidentToSurface.htm) | Creates a new coincident constraint between the sketch point and surface. This forces the point to lie on the surface. |
| [addCollinear](GeometricConstraints_addCollinear.htm) | Creates a new collinear constraint between two lines. |
| [addConcentric](GeometricConstraints_addConcentric.htm) | Creates a new concentric constraint between two circles, arcs, ellipses, or elliptical arcs. |
| [addEqual](GeometricConstraints_addEqual.htm) | Creates a new equal constraint between two lines, or between arcs and circles. |
| [addHorizontal](GeometricConstraints_addHorizontal.htm) | Creates a new horizontal constraint on a line. |
| [addHorizontalPoints](GeometricConstraints_addHorizontalPoints.htm) | Creates a new horizontal constraint between two points. |
| [addLineOnPlanarSurface](GeometricConstraints_addLineOnPlanarSurface.htm) | Creates a new constraint that forces the sketch line to lie on a planar surface. |
| [addLineParallelToPlanarSurface](GeometricConstraints_addLineParallelToPlanarSurface.htm) | Creates a new parallel constraint between a sketch line and a planar surface that will constrain the line to lie on a plane parallel to the specified surface. |
| [addMidPoint](GeometricConstraints_addMidPoint.htm) | Creates a new midpoint constraint between a point and a curve. |
| [addOffset](GeometricConstraints_addOffset.htm) | \*\*RETIRED\*\* Creates an offset constraint, which results in creating a new set of curves that are an offset of the input curves. The returned offset constraint provides access to the created curves and the parameter controlling the offset. |
| [addOffset2](GeometricConstraints_addOffset2.htm) | Creates an offset constraint, which results in creating a new set of curves that are an offset of the input curves. The returned offset constraint object provides access to the created curves and the parameter controlling the offset. |
| [addParallel](GeometricConstraints_addParallel.htm) | Creates a new parallel constraint between two lines. |
| [addPerpendicular](GeometricConstraints_addPerpendicular.htm) | Creates a new perpendicular constraint between two lines. |
| [addPerpendicularToSurface](GeometricConstraints_addPerpendicularToSurface.htm) | Creates a new perpendicular constraint that forces the sketch curve to be perpendicular to the specified surface. Line and spline curves are supported. |
| [addPolygon](GeometricConstraints_addPolygon.htm) | Creates a polygon constraint on existing lines in the sketch. |
| [addRectangularPattern](GeometricConstraints_addRectangularPattern.htm) | Creates a new rectangular pattern in the sketch. |
| [addSmooth](GeometricConstraints_addSmooth.htm) | Creates a new smooth constraint between two curves. One of the curves must be a spline. The other curve can be a spline or any other type of curve. |
| [addSymmetry](GeometricConstraints_addSymmetry.htm) | Creates a new symmetry constraint. |
| [addTangent](GeometricConstraints_addTangent.htm) | Creates a new tangent constraint between two curves. |
| [addTwoSidesOffset](GeometricConstraints_addTwoSidesOffset.htm) | Creates two offset constraints, which results in creating two new sets of curves that are an offset of the input curves on each side of the original set of curves. The returned offset constraint objects provide access to the created curves and the parameters controlling the offsets. |
| [addVertical](GeometricConstraints_addVertical.htm) | Creates a new vertical constraint on a line. |
| [addVerticalPoints](GeometricConstraints_addVerticalPoints.htm) | Creates a new vertical constraint between two points. |
| [classType](GeometricConstraints_classType.htm) | Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType(). |
| [createCircularPatternInput](GeometricConstraints_createCircularPatternInput.htm) | Creates a CircularPatternConstraintInput object. Use properties and methods on this object to define the circular pattern you want to create and then use the Add method, passing in the CircularPatternConstraintInput object. |
| [createOffsetInput](GeometricConstraints_createOffsetInput.htm) | Creates an OffsetConstraintInput object. Use properties and methods on this object to define the offset you want to create and then use the addOffset2 method, passing in the OffsetConstraintInput object, to create the offset. |
| [createRectangularPatternInput](GeometricConstraints_createRectangularPatternInput.htm) | Creates a new RectangularPatternConstraintInput object. Use this object to define the various settings associated with a rectangular pattern in a sketch. Once the pattern is defined you can call the addRectangularPattern method and pass in the input object to create the sketch rectangular pattern. |
| [item](GeometricConstraints_item.htm) | Function that returns the specified sketch constraint using an index into the collection. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [count](GeometricConstraints_count.htm) | Returns the number of constraints in the sketch. |
| [isValid](GeometricConstraints_isValid.htm) | Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference. |
| [objectType](GeometricConstraints_objectType.htm) | This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.   It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType(): |

## Accessed From

[Sketch.geometricConstraints](Sketch_geometricConstraints.htm)

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [API Sample that demonstrates creating sketch lines in various ways.](CreateSketchLines_Sample.htm) | Demonstrates several ways to create sketch lines, including as the result of creating a rectangle. |
| [GeometricConstraints.addConcentric](GeometricConstraints_addConcentric_Sample.htm) | Demonstrates the GeometricConstraints.addConcentric method. |

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |