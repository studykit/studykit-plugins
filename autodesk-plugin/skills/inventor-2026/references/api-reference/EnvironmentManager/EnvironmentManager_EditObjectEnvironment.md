# EnvironmentManager.EditObjectEnvironment Property

Parent Object: [EnvironmentManager](../EnvironmentManager/EnvironmentManager.md)

## Description

This method returns the environment associated with the currently active edit object. This is the environment which is the topmost entry in the Application menu. Since Autodesk Inventor 10, the active environment and EditObjectEnvironment are not necessarily the same. Using parallel environments, one can switch to a parallel environment for the same edit object.

## Syntax

EnvironmentManager.**EditObjectEnvironment**() As [Environment](../Environment/Environment.md)

## Property Value

This is a read only property whose value is an [Environment](../Environment/Environment.md).

## Version

Introduced in version 10
