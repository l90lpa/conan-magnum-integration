#include <Corrade/Utility/Debug.h>
#include <Eigen/Dense>
#include <Magnum/EigenIntegration/GeometryIntegration.h>
#include <Magnum/EigenIntegration/Integration.h>
#include <Magnum/Math/Matrix4.h>
#include <iostream>

using Matrix4 = Magnum::Math::Matrix4<float>;
using namespace Magnum::Math::Literals;
using Magnum::EigenIntegration::cast;
using Quaternion = Magnum::Math::Quaternion<float>;

int main() {
  Matrix4 magnum_mat = Matrix4::rotationX(1.13_radf) *
                       Matrix4::rotationY(-2.2_radf) *
                       Matrix4::rotationZ(3.3_radf);

  auto eigen_mat = cast<Eigen::Matrix4f>(magnum_mat);

  Corrade::Utility::Debug() << "Magnum Matrix:\n" << magnum_mat;
  std::cout << "Eigen Matrix:\n" << eigen_mat << std::endl;

  Matrix4 eigen_to_magnum_mat{eigen_mat};
  Corrade::Utility::Debug() << "Eigen to magnum matrix:\n"
                            << eigen_to_magnum_mat;

  Quaternion mag_quat = Quaternion::fromMatrix(magnum_mat.rotation());
  auto eigen_quat = cast<Eigen::Quaternionf>(mag_quat);

  Corrade::Utility::Debug() << "Magnum quaternion:\n" << mag_quat;
  std::cout << "Eigen quaternion:\n[" << eigen_quat.x() << ", "
            << eigen_quat.y() << ", " << eigen_quat.z() << ", "
            << eigen_quat.w() << "]" << std::endl;

  Quaternion eigen_to_mag_quat{eigen_quat};
  Corrade::Utility::Debug() << "Eigen to magnum quaternion:\n"
                            << eigen_to_mag_quat;

  return 0;
}
