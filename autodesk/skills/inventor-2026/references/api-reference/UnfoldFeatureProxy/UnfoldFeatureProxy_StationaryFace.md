# UnfoldFeatureProxy.StationaryFace Property

Parent Object: [UnfoldFeatureProxy](../UnfoldFeatureProxy/UnfoldFeatureProxy.md)

## Description

Property that returns the Face object that was specified as the stationary face during creation. This property can return Nothing in the case where the face has been consumed by another operation and no longer exists in the model. Rolling back the state of the model to a point where the face exists will allow you to access it.

## Syntax

UnfoldFeatureProxy.**StationaryFace**() As [Face](../Face/Face.md)

## Property Value

This is a read only property whose value is a [Face](../Face/Face.md).

## Version

Introduced in version 2010
