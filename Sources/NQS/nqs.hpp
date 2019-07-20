#include "Machine/rbm_spin.hpp"
#include "Graph/hypercube.hpp"
#include "Hilbert/spins.hpp"
#include "Optimizer/ada_max.hpp"
#include "Sampler/metropolis_local.hpp"
#include <vector>


namespace netket {

class NQS {

    using VectorType = Eigen::Matrix<Complex, Eigen::Dynamic, 1>;
    using MatrixType = Eigen::Matrix<Complex, Eigen::Dynamic, Eigen::Dynamic>;

    int nqubits_;
    Hypercube g;
    /*
    std::shared_ptr<Spin> hi;
    RbmSpin psi;
    MetropolisLocal sa;
    AdaMax op;
    */

    public:

        NQS(int nqubits)
            : nqubits_(nqubits), g(1,1,false) {}

        void applyHadamard(int qubit) {}
        void applyPauliX(int qubit){}
        void applyPauliY(int qubit){}
        void applyPauliZ(int qubit){}
        void applySingleZRotation(int qubit, double theta){}
        void applyControlledZRotation(int controlQubit, int qubit, double theta){}
        void sample(){}
        VectorType getPsiParams(){}

    private:

        /*
        VectorType getPsi_a() {
            RbmSpin::VectorType pars = psi.GetParameters();
            //always "use_a" & "use_b"
            return pars.head(psi.Nvisible());
        }

        VectorType getPsi_b() {
            RbmSpin::VectorType pars = psi.GetParameters();
            //always "use_a" & "use_b"
            return pars.segment(psi.Nvisible(), psi.Nhidden());
        }

        MatrixType getPsi_W() {
            RbmSpin::VectorType pars = psi.GetParameters();
            VectorType Wpars = pars.tail(psi.Nvisible() * psi.Nhidden());
            return Eigen::Map<MatrixType>(Wpars.data(), psi.Nvisible(), psi.Nhidden());
        }
        //void setPsiParams(RbmSpin::VectorType& a, RbmSpin::VectorType& b, RbmSpin::MatrixType& W);
         */
    };

}  // namespace netket