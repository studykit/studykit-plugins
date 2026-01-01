# WorkPlaneProxy.ReferencedEntity Property

Parent Object: [WorkPlaneProxy](../WorkPlaneProxy/WorkPlaneProxy.md)

## Description

Property that returns the referenced WorkPlane in the case where this work plane was created using a referenced component. An example of this is when a work plane is selected as part of a derived part. The HasReferenceComponent property indicates if this work plane is based on a referenced component or not. This property returns Nothing in the case where it is not based on a referenced component.

## Syntax

WorkPlaneProxy.**ReferencedEntity**() As [WorkPlane](../WorkPlane/WorkPlane.md)

## Property Value

This is a read only property whose value is a [WorkPlane](../WorkPlane/WorkPlane.md).

## Version

Introduced in version 5.3
